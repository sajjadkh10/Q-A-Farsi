from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.retriever import QARetriever
from app.generator import AnswerGenerator

app = FastAPI(
    title="سیستم پرسش و پاسخ فارسی",
    description="سیستم هوشمند پاسخ به سوالات به زبان فارسی",
    version="1.0.0"
)

try:
    retriever = QARetriever()
    generator = AnswerGenerator()
except Exception as e:
    raise RuntimeError(f"Failed to initialize components: {str(e)}")


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_qna(req: QuestionRequest):
    try:
        results = retriever.query(req.question)

        if not results or results[0]["score"] < 0.6:
            return {
                "answer": "پاسخی برای سوال شما یافت نشد.",
                "suggested_questions": [r["question"] for r in results[:3]]
            }

        best_match = results[0]
        generated_answer = generator.generate(req.question, best_match["answer"])

        return {
            "answer": generated_answer,
            "source_question": best_match["question"],
            "confidence": best_match["score"],
            "related_questions": [r["question"] for r in results[1:3]]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"خطا در پردازش سوال: {str(e)}"
        )


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "سیستم فعال و آماده به کار است"}