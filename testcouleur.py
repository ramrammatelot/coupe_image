# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:17:17 2023

@author: ram
"""
from matplotlib import pyplot as plt
import cv2
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

image = cv2.imread('nb.png')
df_mean_color = pd.DataFrame()
for idx,i in enumerate(image):
    B_mean, G_mean, R_mean, _ = cv2.mean(image)
    df = pd.DataFrame({'B_mean': B_mean, 'G_mean': G_mean, 'R_mean': R_mean}, index=[idx])
    df_mean_color = pd.concat([df_mean_color, df])
km = KMeans( n_clusters=6)
df_mean_color['label'] = km.fit_predict(df_mean_color)