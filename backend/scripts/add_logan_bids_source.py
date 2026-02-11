from sqlalchemy import text
from backend.app.db.session import SessionLocal

def main():
    db = SessionLocal()
    try:
        sql = text("""
        insert into sources (name, jurisdiction, source_type, base_url, active)
        values (:name, :jurisdiction, :source_type, :base_url, true)
        returning id;
        """)
        source_id = db.execute(sql, {
            "name": "Logan County (OH) - Bid Postings",
            "jurisdiction": "Logan County, OH",
            "source_type": "logan_bids_html",
            "base_url": "https://www.logancountyohio.gov/bids.html",
        }).scalar()

        db.commit()
        print("Inserted Logan bids source_id:", source_id)
    finally:
        db.close()

if __name__ == "__main__":
    main()
