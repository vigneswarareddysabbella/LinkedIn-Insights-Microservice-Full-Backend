from sqlalchemy.orm import Session
from app.models.page import LinkedInPage
from app.services.scraper import scrape_linkedin_page

async def get_or_create_page(db: Session, page_id: str):
    page = db.query(LinkedInPage).filter(
        LinkedInPage.page_id == page_id
    ).first()

    if page:
        return page

    scraped = await scrape_linkedin_page(page_id)

    page = LinkedInPage(
        page_id=scraped["page_id"],
        name=scraped["name"],
        url=scraped["url"],
        followers=scraped["followers"]
    )

    db.add(page)
    db.commit()
    db.refresh(page)

    return page
