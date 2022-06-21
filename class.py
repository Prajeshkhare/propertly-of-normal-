import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print("mean,median and mode is {} , {} and {} respectively".format(height_mean,height_median,height_mode))
print("mean,median and mode is {} , {} and {} respectively".format(weight_mean,weight_median,weight_mode))

height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)
# 1,2 & 3 stard deviation for height

height_first_std_deviation_start ,height_first_std_deviation_end = height_mean-height_std_deviation ,height_mean+height_std_deviation
height_second_std_deviation_start ,height_second_std_deviation_end = height_mean-(2*height_std_deviation) ,height_mean+(2*height_std_deviation)
height_thrid_std_deviation_start ,height_thrid_std_deviation_end = height_mean-(3*height_std_deviation) ,height_mean+(3*height_std_deviation)

# 1,2 & 3 stard deviation for weight

weight_first_std_deviation_start ,weight_first_std_deviation_end = weight_mean-height_std_deviation ,weight_mean+height_std_deviation
weight_second_std_deviation_start ,weight_second_std_deviation_end = weight_mean-(2*height_std_deviation) ,weight_mean+(2*height_std_deviation)
weight_thrid_std_deviation_start ,weight_thrid_std_deviation_end = weight_mean-(3*height_std_deviation) ,weight_mean+(3*height_std_deviation)

# percentage of data within 1,2&3 stadard deviation for height 
height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_thrid_std_deviation_start and result < height_thrid_std_deviation_end]

# percentage of data within 1,2&3 stadard deviation for weight
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_thrid_std_deviation_start and result < weight_thrid_std_deviation_end]

# printing data for height and weight
print("{}% of data for height lies within 1 stadard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 stadard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 stadard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 stadard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 stadard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 stadard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))