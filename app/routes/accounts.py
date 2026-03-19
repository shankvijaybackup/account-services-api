from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas
from decimal import Decimal

router = APIRouter()

@router.get("/{account_id}/balance", response_model=schemas.BalanceResponse)
async def get_balance(account_id: str, db: Session = Depends(get_db)):
    account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, "balance": account.balance, "currency": account.currency, "available": account.available_balance}

@router.get("/{account_id}/transactions")
async def get_transactions(account_id: str, limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    txns = db.query(models.Transaction).filter(models.Transaction.account_id == account_id).order_by(models.Transaction.created_at.desc()).offset(offset).limit(limit).all()
    return {"transactions": txns, "total": len(txns), "limit": limit, "offset": offset}