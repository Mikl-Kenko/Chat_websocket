chat_websocket

application: 
# Life chat

1. Install dependencies:  pip install -r requirements.txt
2. Run Redis-Stack:   docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
3. Start server:  python3 manage.py runserver
4. And can use:   http://0.0.0.0:8000/chat


Work plan:
1. Enable Authentication.
2. Chat layout.
3. Add files in messages.