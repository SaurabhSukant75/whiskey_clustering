# Project Title :- Classiﬁcation of Scotch Whiskeys based on their ﬂavour characteristics by using Spectral Co-Clustering algorithm. Scotch whisky is prized for its complexity and  variety of ﬂavors in the regions of Scotland.









<h1>  Table of Contents: </h1>


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







                  


























              
