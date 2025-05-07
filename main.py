from typing import Optional, Any

from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.post("/vrs/{plan_id}")
def vrsAPI(plan_id: str, data: Optional[dict[str, Any]] = None):
    print("<===== CALL BACK DATA ===>", plan_id,"\n", data)
    return {"plan_id": plan_id, "data": data}
