#!/usr/bin/env python3.7

aws_list = [ ]
aws_list.append("S3")
aws_list.append("EC2")
aws_list.append("Lambda")
print(aws_list)
print(len(aws_list))
del aws_list[0]
del aws_list[1]
print(aws_list)
print(len(aws_list))