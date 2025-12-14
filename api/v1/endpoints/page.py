from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.linkedin_service import get_or_create_page


router = APIRouter()


@router.get("/page/{page_id}")
async def get_page(page_id: str, db: Session = Depends(get_db)):
return await get_or_create_page(db, page_id)


@router.get("/pages")
async def filter_pages(
min_followers: int = 0,
max_followers: int = 1000000,
industry: str | None = None,
db: Session = Depends(get_db)
):
query = db.query(LinkedInPage).filter(
LinkedInPage.followers.between(min_followers, max_followers)
)


if industry:
query = query.filter(LinkedInPage.industry.ilike(f"%{industry}%"))


return query.all()