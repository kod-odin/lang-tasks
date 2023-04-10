#!/bin/bash
metka_ss="0"
outnum=12798
for metka_to in `awk '{print $1}' < 1.txt`
do
	echo $metka_ss - $metka_to - $outnum
	ffmpeg -ss $metka_ss -to $metka_to -i перро.wav $outnum.wav
	
	metka_ss=$metka_to
	((outnum++))
done

