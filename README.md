1. OPENAI_API_KEY or GROQ_API_KEY in .env (we have code for both versions in main.py, data_loader.py and vector_db.py)

2. uv run uvicorn main:app --reload

3. npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery

4. docker run -d --name qdrantRagDB -p 6333:6333 -v "$(pwd)/qdrant_storage:/qdrant/storage" qdrant/qdrant
   command above fill result in random cached string
   qdrant must be run manually from docker or with command below:
   docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant

5. uv run streamlit run streamlit_app.py

6. Payload example for invoking RAG: Ingest PDF function in Inngest:
   {
   "data": {
   "pdf_path": "C:\\Users\\milos\\Desktop\\Cover Letter.pdf"
   }}

7. Payload example for RAG: Query PDF funcion in Inngest:
   {
   "data": {
   "question": "Tell me something about techonologies in Cover Letter?"
   }}

8. during developement if we for example want to change vector dimension from 3072 to 1024 we must execute code in this file delete_docs_collection.py
