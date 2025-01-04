import base64

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

bot_image_data = get_base64_image("images/Botimg.jpg")
bot_template = f'''
<div class="chat-message bot">
    <div class="avatar">
        <img src="data:image/jpeg;base64,{bot_image_data}" 
             style="max-height: 70px; max-width: 70px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{{{MSG}}}}</div>
</div>
'''


userimage_data = get_base64_image("images/Userimg.jpg")
user_template = f'''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/jpeg;base64,{userimage_data}"
        style="max-height: 70px; max-width: 70px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{{{MSG}}}}</div>
</div>
'''

