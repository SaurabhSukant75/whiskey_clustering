# Project Title :- <H>Classiﬁcation of Scotch Whiskeys based on their ﬂavour characteristics by using Spectral Co-Clustering algorithm. Scotch whisky is prized for its complexity and  variety of ﬂavors in the regions of Scotland.</H>









<p><b>  Table of Contents: </b></p>


   <ol>
  <li>Introduction </li>
  <li>Objective</li>
  <li>Data set:</li>
         <ol>
         <li>Source of data set</li>
         <li>Data set discription and feature</li>
          </ol>
   <li>Feature extrection:</li>
         <ol>
         <li>Features</li>
         <li>Latent features</li>
          </ol>
  <li>Algoritham:</li>
            <ol>
         <li>How to choose Algorithm</li>
         <li>spectral co clustering algorithm</li>
          </ol>
  <li>Validation</li>
  <li>Result</li>

</ol>


<h1>INTRODUCTION:-</h1>
         <p>Scotch whisky is prized for its complexity and variety of flavors in  the regions of Scotland where it is produced are believed to have distinct flavor profiles.In this project , we will classify scotch whiskies based on their flavor characteristics.The dataset we’ll be using contains a selection of scotch whiskies from several distilleries, and we’ll attempt to cluster whiskies into groups that are similar in flavor.</p>


<h2>2.OBJECTIVE:-</h2>
   <p>To make cluster of scotch whisky based on their flavour characteristics.</p>





<h2>3.DATA SET:- </h2>
 <p>3.1  source of Data set:-   
 Whisky Advocate is America’s leading whisky publication. It’s a premier source for whisky information, education and entertainment for whisky enthusiasts.The site is one of the most famous whisky webpage. And descriptions included in the dataset are reviewd by authorized whisky reviewers.</p>






<p>3.2 Data set discription and feature:-</p>
         <p>The whisky  dataset contins 86 rows of malt whisky test scores and 17 columns of taste categories and region dataset contains 86 rows of malt whisky location in scotland.The dataset we’ll be using consists of tasting ratings of one readily available single malt scotch whisky from almost every active whisky distillery in Scotland.The resulting dataset has 86 malt whiskies that are scored (dummy variables) between 0 and 4 in 12 different taste categories.The scores have been aggregated from 10 different professional whisky tasters.The taste categories describe whether the whiskies are sweet, smoky, medicinal, spicy, and so on.</p>

<b> for more about data read read_for_data_info.txt file</b>
         
         
         
         
         
         
 <h2>4.Feature extrection:-</h2>   
         <p>Given features are following:<p/>
         <ul>
  <li>Body  </li>
  <li>Sweetness</li>
  <li>Smoky</li>
   <li>Medicinal</li>
  <li>Tobacco</li>
  <li>Honey</li>
  <li>Spicy</li>
  <li>Winey </li>
  <li>Nutty</li>
  <li>Malty</li>
  <li>Fruity</li>
  <li>Floral</li>
</ul>
         <p>Here, we can see 12 features are given and we have to make cluster based on these features.For this,we can find another features based on these features which is known as latent feature. Here,we can check features are independent of each other or not and after finding varience co-varience matrix ,the off diagonal element of varience co-varience matrix is not zero,which means features are not independent of each other because </p>
         
         <b> # Two variables are independent of each other :-iff co-relation coefficient is zero</b>
         
<p>so, as a latent feature i calculate co-relation coefficient matrix based on given features whis is of 86x86 matrix.</p>
<b>open co_realtion_coeff_matrix.pdf file to see the co-relation coefficient matrix and thier plot </b>
                       
                       
                       
                       
 <h2>5. Algoritham:-</h2> 
<h3> <b>5.1 How to choose Algoritham</b></h3>
   <p>Science we only have input vector ,i.e unlabelled data set .so,This is a clear cut unsupervised problem.so,we have to find clustering Algorithm which will best suited for this .</p> 
   <p>so, we can us either <b>k-means clustering or spectral co-clustering Algoritham</b></p>

<h3><b> Spectral Co-clustering Algoritham</b></h3>
   <p>click on the belowlink.<p>
   <p>https://en.wikipedia.org/wiki/Biclustering</p>
 <h2>Result:-</h2>
   <p>Based on variety of flavour characteristics of scotch whisky ,Malt whiskies are categories into five cluster  which are following-</p>
   <p>here,o,1,2,3,4 show the label of class ,they are just dummy variables to describe different cluster.</p>
<p>
   <ul>
 <li><b> index   whisky_name    label_of_class<b></li>
<li>0             AnCnoc            0</li>
<li>1           Auchentoshan          0</li>
<li>2          Balblair               0</li>
<li>3         Bruichladdich           0</li>
<li>4          Bunnahabhain           0</li>
<li>5           Cardhu  0</li>
<li>6    Craigallechie  0</li>
<li>7     Craigganmore  0</li>
<li>8       Dalwhinnie  0</li>
<li>9         Dufftown  0</li>
<li>10       GlenMoray  0</li>
<li>11    Glenallachie  0</li>
<li>12      Glenlossie  0</li>
<li>13    Glenmorangie  0</li>
<li>14     Loch Lomond  0</li>
<li>15      Strathmill  0</li>
<li>16      Tamnavulin  0</li>
<li>17       Tobermory  0</li>
<li>18       Aberfeldy  1</li>
<li>19         Ardmore  1</li>
<li>20        Aultmore  1</li>
<li>21        BenNevis  1</li>
<li>22       Benrinnes  1</li>
<li>23       Benromach  1</li>
<li>24      BlairAthol  1</li>
<li>25        Edradour  1</li>
<li>26       GlenGrant  1</li>
<li>27      GlenScotia  1</li>
<li>28       Glengoyne  1</li>
<li>29        Longmorn  1</li>
<li>..             ... ..</li>
<li>56        GlenSpey  3</li>
<li>57     Glenfiddich  3</li>
<li>58     Glenkinchie  3</li>
<li>59       Glenlivet  3</li>
<li>60       Inchgower  3</li>
<li>61        Linkwood  3</li>
<li>62    RoyalBrackla  3</li>
<li>63        Speyburn  3</li>
<li>64       Teaninich  3</li>
<li>65       Tomintoul  3</li>
<li>66    Tullibardine  3</li>
<li>67        Aberlour  4</li>
<li>68       Auchroisk  4</li>
<li>69       Balmenach  4</li>
<li>70       Dailuaine  4</li>
<li>71         Dalmore  4</li>
<li>72        Deanston  4</li>
<li>73       GlenKeith  4</li>
<li>74     Glendronach  4</li>
<li>75      Glendullan  4</li>
<li>76     Glenfarclas  4</li>
<li>77      Glenrothes  4</li>
<li>78      Glenturret  4</li>
<li>79   Highland Park  4</li>
<li>80       Knochando  4</li>
<li>81        Macallan  4</li>
<li>82        Mortlach  4</li>
<li>83  RoyalLochnagar  4</li>
<li>84         Tomatin  4</li>
<li>85         Tormore  4</li>

</ul>
</p>



<h2>Note:</h2><p>For step by step coding and analysis read the ANALYSIS.PDF</p>




                  


























              
