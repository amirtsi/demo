from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dictionary to store the state of the switch
switch_state = {"on": False}

@app.get("/switch")
async def get_switch_state():
    """
    Endpoint to get the current state of the switch.
    """
    return {"switch_state": switch_state["on"]}

@app.post("/switch/toggle")
async def toggle_switch():
    """
    Endpoint to toggle the state of the switch.
    """
    switch_state["on"] = not switch_state["on"]
    return {"message": "Switch toggled successfully", "switch_state": switch_state["on"]}

@app.post("/switch/{new_state}")
async def set_switch_state(new_state: str):
    """
    Endpoint to set the state of the switch.
    """
    if new_state.lower() not in ["on", "off"]:
        raise HTTPException(status_code=400, detail="Invalid switch state. Use 'on' or 'off'.")

    switch_state["on"] = True if new_state.lower() == "on" else False
    return {"message": f"Switch state set to {new_state}", "switch_state": switch_state["on"]}
