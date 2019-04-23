#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:33:38 2019

@author: tharun
"""
import pandas as pd

def read_data(url="",separator=","):
    df = pd.read_csv(url,sep=separator)
    if(len(df.columns) < 3):
        print("Dataset has less than 3 columns, can't create dataset")
        return None
    else:
        return df

def test_create_dataframe(df,columns = [],column_type=[]):
    
    #checking for function inputs
    if not isinstance(df,pd.DataFrame):
        print("Invalid dataframe")
        return False
    
    #number of columns should be equal to number of column types
    if len(columns)!= len(column_type):
        print("Column names and column types should have equal number of entries")
        return False
    
    #Check if the dataframe and columns have equal number of items    
    dfColumns = list(df.columns) 
    if len(dfColumns) != len(columns):
        print("Number of columns are not the same")
        return False
    
    #check if the column names are matching 
    for column in dfColumns:
        if column not in columns:
            print("Column names do not match")
            return False
    
    #check if the datatypes are matching
    for column in dfColumns:
        if  df[column].dtype != column_type[columns.index(column)]:
            print("Datatypes do not match")
            return False
    
    #check for the number of rows in dataset
    if len(df) < 10:
        print("DataFrame consists of less than 10 rows")
        return False
    
    return True

    
