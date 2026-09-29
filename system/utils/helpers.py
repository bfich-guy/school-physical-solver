from fastapi import FastAPI, APIRouter


#region Server helpers

def include_routers(
    *,
    app: FastAPI,
    routers_list: list[APIRouter],
) -> None:

    for router in routers_list:
        app.include_router(router=router)

#endregion
