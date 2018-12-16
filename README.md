# Project Title :- Classiﬁcation of Scotch Whiskeys based on their ﬂavour characteristics by using Spectral Co-Clustering algorithm. Scotch whisky is prized for its complexity and  variety of ﬂavors in the regions of Scotland.









####################### ####         ########               Table of Contents:       ###   #############   ###################







         # 1.Introduction
         # 2.Objective
         # 3.Data set:
              3.1 Source of data set
              3.2 Data set discription and feature
              
          #4.Feature extrection:
              4.1 Latent feature
         # 5. Algoritham:
              5.1 spectral co clustering algorithm
          #6. Validation
          #7.Result





#INTRODUCTION:-Scotch whisky is prized for its complexity and variety of flavors in  the regions of Scotland where it is produced are believed to have distinct flavor profiles.In this project , we will classify scotch whiskies based on their flavor characteristics.The dataset we’ll be using contains a selection of scotch whiskies from several distilleries, and we’ll attempt to cluster whiskies into groups that are similar in flavor.


#2.OBJECTIVE:-To make cluster of scotch whisky based on their flavour characteristics.









#3.DATA SET:3.1 source of Data set-Whisyk Advocate:
Whisky Advocate is America’s leading whisky publication. It’s a premier source for whisky information, education and entertainment for whisky enthusiasts.

The site is one of the most famous whisky webpage. And descriptions included in the dataset are reviewd by authorized whisky reviewers.






3.2 Data set discription and feature:-The whisky  dataset contins 86 rows of malt whisky test scores and 17 columns of taste categories and region dataset contains 86 rows of malt whisky location in scotland.The dataset we’ll be using consists of tasting ratings of one readily available single malt scotch whisky from almost every active whisky distillery in Scotland.The resulting dataset has 86 malt whiskies that are scored (dummy variables) between 0 and 4 in 12 different taste categories.The scores have been aggregated from 10 different professional whisky tasters.The taste categories describe whether the whiskies are sweet, smoky, medicinal, spicy, and so on.












#df.info()                                #####################################################################
<class 'pandas.core.frame.DataFrame'>     #####################################################################
RangeIndex: 86 entries, 0 to 85           #####################################################################
Data columns (total 19 columns):          #####################################################################
RowID                86 non-null int64    #####################################################################
Distillery           86 non-null object   #####################################################################
Body                 86 non-null int64    #####################################################################
Sweetness            86 non-null int64    #####################################################################
Smoky                86 non-null int64    #####################################################################
Medicinal            86 non-null int64    #####################################################################
Tobacco              86 non-null int64    #####################################################################
Honey                86 non-null int64    #####################################################################
Spicy                86 non-null int64    #####################################################################
Winey                86 non-null int64    #####################################################################
Nutty                86 non-null int64    #####################################################################
Malty                86 non-null int64    #####################################################################
Fruity               86 non-null int64    #####################################################################
Floral               86 non-null int64    #####################################################################
Postcode             86 non-null object   #####################################################################
 Latitude            86 non-null int64    #####################################################################
 Longitude           86 non-null int64    #####################################################################
Region               85 non-null object   #####################################################################
disteliries_group    86 non-null int32    #####################################################################
dtypes: int32(1), int64(15), object(3)    #####################################################################
























#  df.head()
RowID Distillery  Body  Sweetness  Smoky  Medicinal  Tobacco  Honey  Spicy  \
0      1  Aberfeldy     2          2      2          0        0      2      1   
1      2   Aberlour     3          3      1          0        0      4      3   
2      3     AnCnoc     1          3      2          0        0      2      0   
3      4     Ardbeg     4          1      4          4        0      0      2   
4      5    Ardmore     2          2      2          0        0      1      1   

   Winey  Nutty  Malty  Fruity  Floral     Postcode   Latitude   Longitude  \
0      2      2      2       2       2   \tPH15 2EB     286580      749680   
1      2      2      3       3       2   \tAB38 9PJ     326340      842570   
2      0      2      2       3       2    \tAB5 5LI     352960      839320   
3      0      1      2       1       0   \tPA42 7EB     141560      646220   
4      1      2      3       1       1   \tAB54 4NH     355350      829140   

    Region  disteliries_group  
0   Speyside                  1  
1  Highlands                  4  
2      Islay                  0  
3  Highlands                  2  
4    Islands                  1  

              
