# For Loop in Sh

python="/storage/buhm/anaconda3/envs/buhm_env/bin/python"

for i in {1..22}
do
        ${python} script.py Matched_INN_GT.chr${i}.r0.8.raw chr${i}_r08.pickle  &
done
