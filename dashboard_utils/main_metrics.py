import datetime

import streamlit as st
import pandas as pd

import wandb

from dashboard_utils.time_tracker import _log, simple_time_tracker

WANDB_REPO = "learning-at-home/Main_metrics"
CACHE_TTL = 120  # note: in the text, we claim that this plot is updated every few minutes


@st.cache(ttl=CACHE_TTL)
@simple_time_tracker(_log)
def get_main_metrics():
    wandb.login(anonymous="must")
    api = wandb.Api()
    runs = api.runs(WANDB_REPO)
    run = runs[0]
    history = run.scan_history(keys=["step", "loss", "alive peers", "_timestamp"])

    steps = []
    losses = []
    alive_peers = []
    dates = []
    for row in history:
        steps.append(row["step"])
        losses.append(row["loss"])
        alive_peers.append(row["alive peers"])
        dates.append(datetime.datetime.utcfromtimestamp(row["_timestamp"]))

    return pd.DataFrame({"steps": steps, "training loss": losses, "active participants": alive_peers, "wall time": dates})
