import requests
import json
import re
import telebot
from telebot import types
import threading

BOT_TOKEN = "token botttttttttttt"# توكن البوت هنا 
bot = telebot.TeleBot(BOT_TOKEN)

user_data = {}
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.chat.id
    user_data[user_id] = {}
    
    welcome_text = """
    [☾★ ] **مرحباً بك في بوت INsta✈Devils !**
    
     **كيفية الاستخدام:**
    1. أرسل رابط المنشور الذي تريد معلوماته
    2. أرسل sessionid و userid عندما يطلب منك
    3. احصل على المعلومات كاملة!
    
    🔍 **للمطورين:**
    - جلب معلومات أي منشور على إنستغرام
 - Dev @rxr41
Code 🇪🇸 البراري 
    - الحصول على روابط الوسائط عالية الجودة
    """
    
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

def extract_media_id(post_url):
    try:
        if "/p/" not in post_url:
            return None
        
        match = re.search(r'/p/([^/]+)', post_url)
        if match:
            shortcode = match.group(1)
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
            media_id = 0
            
            for char in shortcode:
                media_id = (media_id * 64) + alphabet.index(char)
                
            return str(media_id)
        
        return None
        
    except Exception as e:
        return None

def get_instagram_post_info(media_id, session_id, user_id):
    try:
        url = f"https://i.instagram.com/api/v1/media/{media_id}/info/"
        
        headers = {
            'User-Agent': "Instagram 309.1.0.41.113 Android",
            'X-IG-App-ID': "567067343352427",
            'IG-U-DS-USER-ID': user_id,
            'IG-INTENDED-USER-ID': user_id,
            'X-IG-Android-ID': "android-6b89ea4c1e25699c",
            'Authorization': "Bearer IGT:2:eyJkc191c2VyX2lkIjoiNDQzMzg0Mzc0NTciLCJzZXNzaW9uaWQiOiI0NDMzODQzNzQ1NyUzQWlGVkIwZHBPQXJnNmVpJTNBOSUzQUFZaWUtTjd2dy1yZS1nQVR4RjMxZWVNOURRLTkzUzU4Zk0wU2pTYmR6ZyJ9",
            'Cookie': f"sessionid={session_id}; ds_user_id={user_id};"
        }

        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
            
    except Exception as e:
        return None

def send_post_info(chat_id, post_data, media_id):
    """إرسال معلومات المنشور إلى المستخدم"""
    try:
        if not post_data or 'items' not in post_data or not post_data['items']:
            bot.send_message(chat_id, "❌ لم أتمكن من جلب معلومات المنشور")
            return
        
        item = post_data['items'][0]
        user_info = item.get('user', {})
        
        message_text = f"""
☜☆☞ **معلومات المنشور**

👤 **المستخدم:** @{user_info.get('username', 'غير معروف')}
📛 **الاسم:** {user_info.get('full_name', 'غير معروف')}

📈 **الإحصائيات:**
❤️  الإعجابات: {item.get('like_count', 0):,}
💬 التعليقات: {item.get('comment_count', 0):,}
📤 المشاركات: {item.get('reshare_count', 0):,}

🆔 **Media ID:** `{media_id}`
        """
             
        media_type = item.get('media_type', 1)
        if media_type == 1:
            message_text += "\n📸 **نوع المحتوى:** صورة"
        elif media_type == 2:
            message_text += "\n🎥 **نوع المحتوى:** فيديو"
        elif media_type == 8:
            message_text += "\n🖼️ **نوع المحتوى:** كاروسيل"
              
        caption = item.get('caption', {}).get('text', '')
        if caption:
            message_text += f"\n\n📝 **الوصف:**\n{caption[:300]}{'...' if len(caption) > 300 else ''}"             
        bot.send_message(chat_id, message_text, parse_mode='Markdown')        
        
        if media_type == 1 and 'image_versions2' in item:
            candidates = item['image_versions2'].get('candidates', [])
            if candidates:
                best_quality = max(candidates, key=lambda x: x.get('width', 0))
                bot.send_photo(chat_id, best_quality['url'])
        
        with open(f'post_{media_id}.json', 'w', encoding='utf-8') as f:
            json.dump(post_data, f, indent=2, ensure_ascii=False)
        
        with open(f'post_{media_id}.json', 'rb') as f:
            bot.send_document(chat_id, f, caption="📁 البيانات الكاملة للمنشور")
            
    except Exception as e:
        bot.send_message(chat_id, f"[ ✡ ]{str(e)}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    text = message.text.strip()
    
    if user_id not in user_data:
        user_data[user_id] = {}
  
    if 'instagram.com' in text and '/p/' in text:
        media_id = extract_media_id(text)
        if media_id:
            user_data[user_id]['media_id'] = media_id
            user_data[user_id]['post_url'] = text
            
            bot.send_message(user_id, """
✈ **تم التعرف على رابط المنشور!**

🔐 **الآن أحتاج معلومات الجلسة:**

1. **sessionid** - 
2. **user id** - 

 **أرسل sessionid الآن:**
            """)
        else:
            bot.send_message(user_id, "❌ رابط المنشور غير صحيح")
       
    elif 'sessionid' not in user_data[user_id] and len(text) > 50:
        user_data[user_id]['session_id'] = text
        bot.send_message(user_id, "✅ **تم حفظ sessionid**\n\n👤 الآن أرسل **user id**:")
        
    elif 'session_id' in user_data[user_id] and 'user_id' not in user_data[user_id]:
        user_data[user_id]['user_id'] = text               
        media_id = user_data[user_id].get('media_id')
        session_id = user_data[user_id].get('session_id')
        user_id_val = user_data[user_id].get('user_id')
        
        if media_id and session_id and user_id_val:
            bot.send_message(user_id, "⏳ **جاري جلب معلومات المنشور...**")            
            
            def fetch_data():
                post_data = get_instagram_post_info(media_id, session_id, user_id_val)
                send_post_info(user_id, post_data, media_id)               
                if user_id in user_data:
                    del user_data[user_id]
            
            thread = threading.Thread(target=fetch_data)
            thread.start()
        else:
            bot.send_message(user_id, "❌ البيانات غير مكتملة")
    
    else:
        bot.send_message(user_id, """
📋 **أرسل لي رابط منشور إنستغرام:**

الحصول على جميع المعلوماته 
        """, parse_mode='Markdown')

print("🤖 البوت يعمل...")
bot.polling(none_stop=True)