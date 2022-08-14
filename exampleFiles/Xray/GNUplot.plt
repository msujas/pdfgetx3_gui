reset
set xlabel 'Q  (Å^-1)'
set ylabel 'Diff. CS [barns/sr/atom]'
set xrange [0:23.5]
set style line 1 lt 1ps 0 lc 1
set style line 2 lt 1ps 0 lc 2
x=0
y=0
i=-1
plot \
'LaB6_0p4mm_011_av10_monitor.soq' u 1:((column(2)+0.0)+0.0) title 'LaB6_0p4mm_011_av10_monitor.soq' w l ls 1, \
'LaB6_0p4mm_011_av10_monitor.int01' u 1:((column(2)+0.0)+0.0) title 'LaB6_0p4mm_011_av10_monitor.int01' w l ls 2
