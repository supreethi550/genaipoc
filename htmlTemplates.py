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

[data-testid="stAppViewContainer"]{
    background: url('./assets/BackgroundImage.png') no-repeat;
    background-size: 'cover'
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://tse2.mm.bing.net/th?id=OIP.hKzqllvBJMsSdBXNuyBy9wHaIY&pid=Api&P=0&h=180" alt="image">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://tse4.mm.bing.net/th?id=OIP.awAiMS1BCAQ2xS2lcdXGlwHaHH&pid=Api&P=0&h=180" alt="image">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
