from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

df = pd.read_csv("./data/titanic.csv")
