import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import statistics

df=pd.read_csv("StudentsPerformance.csv")
math_score=df["math score"].tolist()
reading_score=df["reading score"].tolist()
writing_score=df["writing score"].tolist()

mmean=statistics.mean(math_score)
mmedian=statistics.median(math_score)
mmode=statistics.mode(math_score)
mstd_deviation=statistics.stdev(math_score)

rmean=statistics.mean(reading_score)
rmedian=statistics.median(reading_score)
rmode=statistics.mode(reading_score)
rstd_deviation=statistics.stdev(reading_score)

wmean=statistics.mean(writing_score)
wmedian=statistics.median(writing_score)
wmode=statistics.mode(writing_score)
wstd_deviation=statistics.stdev(writing_score)

print("The Mean(Average) of Math Score =", mmean)
print("The Median of Math Score =", mmedian)
print("The Mode of Math Score =", mmode)
print("The Standard Deviation of Math Score =", mstd_deviation)

print("The Mean(Average) of Reading Score =", rmean)
print("The Median of Reading Score =", rmedian)
print("The Mode of Reading Score =", rmode)
print("The Standard Deviation of Reading Score =", rstd_deviation)

print("The Mean(Average) of Writing Score =", wmean)
print("The Median of Writing Score =", wmedian)
print("The Mode of Writing Score =", wmode)
print("The Standard Deviation of Writing Score =", wstd_deviation)

mfirst_std_dev_start,mfirst_std_dev_end=mmean-mstd_deviation,mmean+mstd_deviation
msecond_std_dev_start,msecond_std_dev_end=mmean-(2*mstd_deviation),mmean+(2*mstd_deviation)
mthird_std_dev_start,mthird_std_dev_end=mmean-(3*mstd_deviation),mmean+(3*mstd_deviation)

rfirst_std_dev_start,rfirst_std_dev_end=rmean-rstd_deviation,rmean+rstd_deviation
rsecond_std_dev_start,rsecond_std_dev_end=rmean-(2*rstd_deviation),rmean+(2*rstd_deviation)
rthird_std_dev_start,rthird_std_dev_end=rmean-(3*rstd_deviation),rmean+(3*rstd_deviation)

wfirst_std_dev_start,wfirst_std_dev_end=wmean-wstd_deviation,wmean+wstd_deviation
wsecond_std_dev_start,wsecond_std_dev_end=wmean-(2*wstd_deviation),wmean+(2*wstd_deviation)
wthird_std_dev_start,wthird_std_dev_end=wmean-(3*wstd_deviation),wmean+(3*wstd_deviation)

mvalues_under_first_std_dev=[answer for answer in math_score if answer > mfirst_std_dev_start and answer < mfirst_std_dev_end]
mvalues_under_second_std_dev=[answer for answer in math_score if answer > msecond_std_dev_start and answer < msecond_std_dev_end]
mvalues_under_third_std_dev=[answer for answer in math_score if answer > mthird_std_dev_start and answer < mthird_std_dev_end]

rvalues_under_first_std_dev=[answer for answer in reading_score if answer > rfirst_std_dev_start and answer < rfirst_std_dev_end]
rvalues_under_second_std_dev=[answer for answer in reading_score if answer > rsecond_std_dev_start and answer < rsecond_std_dev_end]
rvalues_under_third_std_dev=[answer for answer in reading_score if answer > rthird_std_dev_start and answer < rthird_std_dev_end]

wvalues_under_first_std_dev=[answer for answer in writing_score if answer > wfirst_std_dev_start and answer < wfirst_std_dev_end]
wvalues_under_second_std_dev=[answer for answer in writing_score if answer > wsecond_std_dev_start and answer < wsecond_std_dev_end]
wvalues_under_third_std_dev=[answer for answer in writing_score if answer > wthird_std_dev_start and answer < wthird_std_dev_end]

print("{}% of the data lies between first std_deviation of math score".format(len(mvalues_under_first_std_dev)*100/len(math_score)))
print("{}% of the data lies between second std_deviation of math score".format(len(mvalues_under_second_std_dev)*100/len(math_score)))
print("{}% of the data lies between third std_deviation of math score".format(len(mvalues_under_third_std_dev)*100/len(math_score)))

print("{}% of the data lies between first std_deviation of reading score".format(len(rvalues_under_first_std_dev)*100/len(reading_score)))
print("{}% of the data lies between second std_deviation of reading score".format(len(rvalues_under_second_std_dev)*100/len(reading_score)))
print("{}% of the data lies between third std_deviation of reading score".format(len(rvalues_under_third_std_dev)*100/len(reading_score)))

print("{}% of the data lies between first std_deviation of writing score".format(len(wvalues_under_first_std_dev)*100/len(writing_score)))
print("{}% of the data lies between second std_deviation of writing score".format(len(wvalues_under_second_std_dev)*100/len(writing_score)))
print("{}% of the data lies between third std_deviation of writing score".format(len(wvalues_under_third_std_dev)*100/len(writing_score)))

fig=ff.create_distplot([math_score],["Math Score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mmean,mmean], y=[0,0.025], mode="lines", name="Math Score Mean"))
fig.add_trace(go.Scatter(x=[mfirst_std_dev_start,mfirst_std_dev_start], y=[0,0.025], mode="lines", name="1st std_devaition start of math score"))
fig.add_trace(go.Scatter(x=[mfirst_std_dev_end,mfirst_std_dev_end], y=[0,0.025], mode="lines", name="1st std_devaition end of math score"))
fig.add_trace(go.Scatter(x=[msecond_std_dev_start,msecond_std_dev_start], y=[0,0.025], mode="lines", name="2nd std_devaition start of math score"))
fig.add_trace(go.Scatter(x=[msecond_std_dev_end,msecond_std_dev_end], y=[0,0.025], mode="lines", name="2nd std_devaition end of math score"))
fig.add_trace(go.Scatter(x=[mthird_std_dev_start,mthird_std_dev_start], y=[0,0.025], mode="lines", name="3rd std_devaition start of math score"))
fig.add_trace(go.Scatter(x=[mthird_std_dev_end,mthird_std_dev_end], y=[0,0.025], mode="lines", name="3rd std_devaition end of math score"))
fig.show()

fig=ff.create_distplot([reading_score],["Reading Score"], show_hist=False)
fig.add_trace(go.Scatter(x=[rmean,rmean], y=[0,0.025], mode="lines", name="Reading Score Mean"))
fig.add_trace(go.Scatter(x=[rfirst_std_dev_start,rfirst_std_dev_start], y=[0,0.025], mode="lines", name="1st std_devaition start of reading score"))
fig.add_trace(go.Scatter(x=[rfirst_std_dev_end,rfirst_std_dev_end], y=[0,0.025], mode="lines", name="1st std_devaition end of reading score"))
fig.add_trace(go.Scatter(x=[rsecond_std_dev_start,rsecond_std_dev_start], y=[0,0.025], mode="lines", name="2nd std_devaition start of reading score"))
fig.add_trace(go.Scatter(x=[rsecond_std_dev_end,rsecond_std_dev_end], y=[0,0.025], mode="lines", name="2nd std_devaition end of reading score"))
fig.add_trace(go.Scatter(x=[rthird_std_dev_start,rthird_std_dev_start], y=[0,0.025], mode="lines", name="3rd std_devaition start of reading score"))
fig.add_trace(go.Scatter(x=[rthird_std_dev_end,rthird_std_dev_end], y=[0,0.025], mode="lines", name="3rd std_devaition end of reading score"))
fig.show()

fig=ff.create_distplot([writing_score],["Writing Score"], show_hist=False)
fig.add_trace(go.Scatter(x=[wmean,wmean], y=[0,0.025], mode="lines", name="Writing Score Mean"))
fig.add_trace(go.Scatter(x=[wfirst_std_dev_start,wfirst_std_dev_start], y=[0,0.025], mode="lines", name="1st std_devaition start of writing score"))
fig.add_trace(go.Scatter(x=[wfirst_std_dev_end,wfirst_std_dev_end], y=[0,0.025], mode="lines", name="1st std_devaition end of writing score"))
fig.add_trace(go.Scatter(x=[wsecond_std_dev_start,wsecond_std_dev_start], y=[0,0.025], mode="lines", name="2nd std_devaition start of writing score"))
fig.add_trace(go.Scatter(x=[wsecond_std_dev_end,wsecond_std_dev_end], y=[0,0.025], mode="lines", name="2nd std_devaition end of writing score"))
fig.add_trace(go.Scatter(x=[wthird_std_dev_start,wthird_std_dev_start], y=[0,0.025], mode="lines", name="3rd std_devaition start of writing score"))
fig.add_trace(go.Scatter(x=[wthird_std_dev_end,wthird_std_dev_end], y=[0,0.025], mode="lines", name="3rd std_devaition end of writing score"))
fig.show()