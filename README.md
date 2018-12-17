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
 <p><b>3.1  source of Data set:- </b> <p>http://whiskyadvocate.com/</p> 
 Whisky Advocate is America’s leading whisky publication. It’s a premier source for whisky information, education and entertainment for whisky enthusiasts.The site is one of the most famous whisky webpage. </p>






<p><b>3.2 Data set discription and feature:-</b></p>
         <p>The<b> whisky  dataset </b>contins 86 rows of malt whisky test scores and 17 columns of taste categories and <b>region dataset </b>contains 86 rows of active whisky distillery location in scotland.The dataset we’ll be using consists of tasting ratings of one readily available single malt scotch whisky from almost every active whisky distillery in Scotland.The resulting dataset has 86 malt whiskies that are scored (dummy variables) between 0 and 4 in 12 different taste categories.The scores have been aggregated from 10 different professional whisky tasters.The taste categories describe whether the whiskies are sweet, smoky, medicinal, spicy, and so on.</p>

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
         <p>Here, we can see 12 features are given and we have to make cluster based on these features.Here,I tried to find out a latent features which can well discribed all 12 features.For this,I find varience co-varience matrix for checking features are independent of each other or not and after finding varience co-varience matrix ,the off diagonal element of varience co-varience matrix is not zero,which means features are not independent of each other.for more information click here https://en.wikipedia.org/wiki/Covariance_matrix </p>
         
         <b> # Two variables are independent of each other :-iff co-relation coefficient is zero</b>
         
<p>so, as a latent feature i calculate co-relation coefficient matrix based on given features whis is of 86x86 matrix.</p>
<b>open co_realtion_coeff_matrix.pdf file to see the co-relation coefficient matrix and thier plot </b>
                       
                       
                       
                       
 <h2>5. Algoritham:-</h2> 
<h3> <b>5.1 How to choose Algoritham</b></h3>
   <p>Science we only have input vector ,i.e unlabelled data set .so,This is a clear cut unsupervised learning problem.so,we have to find clustering Algorithm which will best suited for this .</p> 
   <p>so, we can us either <b>k-means clustering or spectral co-clustering Algoritham</b></p>

<h3><b> Spectral Co-clustering Algoritham</b></h3>
   <p>click on the belowlink.<p>
   <p>https://en.wikipedia.org/wiki/Biclustering</p>
 <h2>Result:-</h2>
   <p>Based on variety of flavour characteristics of scotch whisky ,Malt whiskies from 86 different distillery  are categories into five cluster  which are following-</p>
   <p>(here,o,1,2,3,4 show the label of class ,they are just dummy variables to describe different cluster.0-->1st cluster,1-->2nd cluster,2-->3rd cluster and so on...)</p>
   
<p>
   <b>  whisky_name   --->label_of_class<b>
   <ul>

<li>            AnCnoc   --->         0</li>
<li>         Auchentoshan --->         0</li>
<li>         Balblair    --->           0</li>
<li>        Bruichladdich  --->         0</li>
<li>          Bunnahabhain --->          0</li>
<li>           Cardhu--->  0</li>
<li>    Craigallechie ---> 0</li>
<li>     Craigganmore ---> 0</li>
<li>      Dalwhinnie ---> 0</li>
<li>         Dufftown--->  0</li>
<li>       GlenMoray ---> 0</li>
<li>    Glenallachie ---> 0</li>
<li>      Glenlossie ---> 0</li>
<li>    Glenmorangie ---> 0</li>
<li>     Loch Lomond ---> 0</li>
<li>      Strathmill ---> 0</li>
<li>      Tamnavulin ---> 0</li>
<li>       Tobermory ---> 0</li>
<li>       Aberfeldy ---> 1</li>
<li>         Ardmore ---> 1</li>
<li>       Aultmore  --->1</li>
<li>        BenNevis ---> 1</li>
<li>       Benrinnes ---> 1</li>
<li>       Benromach  --->1</li>
<li>      BlairAthol ---> 1</li>
<li>        Edradour ---> 1</li>
<li>       GlenGrant ---> 1</li>
<li>      GlenScotia ---> 1</li>
<li>       Glengoyne ---> 1</li>
<li>        Longmorn ---> 1</li>
<li>..             --->... ..</li>
<li>        GlenSpey ---> 3</li>
<li>     Glenfiddich ---> 3</li>
<li>     Glenkinchie ---> 3</li>
<li>       Glenlivet ---> 3</li>
<li>       Inchgower ---> 3</li>
<li>        Linkwood ---> 3</li>
<li>    RoyalBrackla ---> 3</li>
<li>        Speyburn ---> 3</li>
<li>       Teaninich ---> 3</li>
<li>       Tomintoul ---> 3</li>
<li>    Tullibardine ---> 3</li>
<li>        Aberlour ---> 4</li>
<li>       Auchroisk ---> 4</li>
<li>       Balmenach ---> 4</li>
<li>     Dailuaine ---> 4</li>
<li>         Dalmore ---> 4</li>
<li>        Deanston ---> 4</li>
<li>       GlenKeith ---> 4</li>
<li>     Glendronach ---> 4</li>
<li>      Glendullan ---> 4</li>
<li>     Glenfarclas ---> 4</li>
<li>      Glenrothes ---> 4</li>
<li>      Glenturret ---> 4</li>
<li>   Highland Park ---> 4</li>
<li>       Knochando ---> 4</li>
<li>        Macallan ---> 4</li>
<li>        Mortlach ---> 4</li>
<li>  RoyalLochnagar ---> 4</li>
<li>         Tomatin ---> 4</li>
<li>         Tormore ---> 4</li>

</ul>
</p>



<h2>Note:</h2><p>For step by step coding and analysis read the ANALYSIS.PDF</p>
                                   <p>THANK YOU!<p>



                  


























              
