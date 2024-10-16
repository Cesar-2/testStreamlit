"""
# My first app
Here's our first attempt at using data to create a table:
"""
from datetime import datetime
import streamlit as st
import pandas as pd

st.title("My first app")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

st.sidebar.write("This is a sidebar")
st.sidebar.button("Press me")

import asyncio        
import streamlit as st     
import time
from functools import partial
from datetime import datetime

def clock(field, name, starttime):
    tdelta =  datetime.now().replace(microsecond=0) - starttime.replace(microsecond=0)
    minutes, seconds = divmod(int(tdelta.total_seconds()), 60)      
    hours, minutes = divmod(minutes, 60)                                                            
    field.metric(name, f"{hours}:{minutes:02d}:{seconds:02d}")

async def run_jobs(job_list):
    while True:
        for job in job_list:
            job()
        # Not sure why asyncio.sleep was used here...
        time.sleep(0.1)
# Placeholder Fields for Timers

all_tasks = st.empty()
jobs = []

# Jobs are queued for the fields
jobs.append(partial(clock, all_tasks, "COL", datetime.now()))

if jobs:
    with st.spinner("Running..."):
        st.sidebar.write("Time elapsed")
        asyncio.run(run_jobs(jobs))