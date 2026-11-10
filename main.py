import os
import aiohttp
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI(title="Shopify Gateway Checker - Fresh Instance", version="1.0.0")

class CheckPayload(BaseModel):
    card: str
    amount: float = 1.0

@app.post("/shopii/check")
async def fresh_gateway_check(payload: CheckPayload, request: Request):
    card_data = payload.card.strip()
    if "|" not in card_data:
        raise HTTPException(status_code=400, detail="Format required: CC|MM|YY|CVV")
    
    cc, mm, yy, cvv = card_data.split("|")
    
    # *Core processing logic for validation request*
    return {
        "status": "APPROVED",
        "bin": cc[:6],
        "message": "Fresh gateway endpoint operational and ready"
    }

@app.get("/shopii")
async def health_check():
    return {"status": "online", "service": "Fresh Gateway Backend"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
  
