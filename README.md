1. OPENAI_API_KEY or GROQ_API_KEY in .env (we have code for both versions in main.py, data_loader.py and vector_db.py) (Current code version is with GROK_API_KEY, link: https://console.groq.com/keys)

2. uv run uvicorn main:app --reload

3. npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery

4. docker run -d --name qdrantRagDB -p 6333:6333 -v "$(pwd)/qdrant_storage:/qdrant/storage" qdrant/qdrant
   command above fill result in random cached string
   Docker desktop will get image
   qdrant must be run manually from docker or with command below:
   docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant

5. uv run streamlit run streamlit_app.py (This is for frontend part of application)

6. In Ingest UI, payload example for invoking RAG: Ingest PDF function in Inngest:
   {
   "data": {
   "pdf_path": "C:\\Users\\milos\\Desktop\\Cover Letter.pdf"
   }}

7. In Ingest UI, payload example for RAG: Query PDF funcion in Inngest:
   {
   "data": {
   "question": "Tell me something about techonologies in Cover Letter?"
   }}

8. During developement if we for example want to change vector dimension from 3072 to 1024 we must execute code in this file delete_docs_collection.py with this command: uv run python delete_docs_collection.py


9. Changing the LLM model: 
In main.py we currently use "model": "openai/gpt-oss-20b"
Available models are:
- openai/gpt-oss-20b (fast and cheap, recommended)
- openai/gpt-oss-120b (higher quality)
- qwen/qwen3.8-27b
The list is shortened. You can see all other models at: GET https://api.groq.com/openai/v1/models.

Note: the gpt-oss models are reasoning models. Part of max_tokens: 1024 can go to "reasoning", but for a short answer it should be enough. If the answer you get is empty or truncated, increase max_tokens to about 2048.