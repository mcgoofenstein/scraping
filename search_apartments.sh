#!/usr/bin/env bash
MR_HYDE="." #$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
while true; do
echo "CL DOWNLOADER RUNNING ON THIS TERMINAL"
echo "$(date) - search_apartments executed" >> main.log
if pgrep python>/dev/null
then
echo "$(date) - cl_checker is running - " >> main.log
else
python $MR_HYDE/get_cl.py --query "2 BR" --maxAsk 2300 --bedrooms 2 &
echo "search executed at $(date)" >> main.log
fi
sleep 3600
done

