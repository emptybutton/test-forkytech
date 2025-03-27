from fastapi import Query


page_number_query = Query(alias="pageNumber", ge=0)
