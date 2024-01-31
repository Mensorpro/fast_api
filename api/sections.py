import fastapi

router = fastapi.APIRouter()


@router.get("/sections/{secttion_id}", tags=["sections"])
def get_sections():
    return {"courses": "courses"}

@router.get("/sections/{section_id}/content-blocks", tags=["sections"])
def get_sections_content_block():
    return {"courses": "courses"}


@router.get("/content-blocks/{section_id}", tags=["sections"])
def get_content_block():
    return {"courses": "courses"}



