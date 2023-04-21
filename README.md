#PARA Dataset

---
### Paper：Personalized Image Aesthetics Assessment with Rich Attributes(PARA)
Author: Yuzhe Yang, Liwu Xu, Leida Li, Nan Qie, Yaqian Li, Peng Zhang and Yandong Guo.  
Project Page:  https://cv-datasets.institutecv.com/#/data-sets  

### File Structure  

```
PARA  
│  README.md: including introduction to PARA database and license.
│  
└─imgs/
│   session1/
│        iaa_pub1_.jpg
│        iaa_pub2_.jpg
│        ...
│   session2/
│        iaa_pub71_.jpg
│        iaa_pub72_.jpg
│        ...
│   ...  
│       
└─annotation/  
	PARA-Images.csv    : personalized aesthetic attributes score annotation file for all images.
    PARA-UserInfo.csv  : desensitized subject information including user id, age, gender, etc.  
    PARA-GiaaTest.csv  : score distribution annotation for testing GIAA model with PARA.
    PARA-GiaaTrain.csv : score distribution annotation for training GIAA model with PARA.
```

###Annotation Explanation of PIAA

```
PIAA annotation files include: PARA-Images.csv

col 0: session ID.
col 1: imageName.
col 2: user id, "PARA-Images.csv" and "PARA-UserInfo.csv" are related by user id.
col 3: image aesthetic score.
col 4: image quality score.
col 5: image composition score.
col 6: color score.
col 7: depth-of-field score.
col 8: content score.
col 9: light score.
col 10: isObjectEmphasis, 0 means False and 1 means True.
col 11: image emotion class label.
col 12: difficulty of judgement score. -1, 0, 1 represent easy, normal, difficult respectively.
col 13: content preference score.
col 14: willingness to share score.
col 15: scene category label.
```

###Annotation Explanation of Subject Information

```
PIAA annotation files include: PARA-UserInfo.csv

col 0: user id, "PARA-Images.csv" and "PARA-UserInfo.csv" are related by user id.
col 1: age interval.
col 2: gender class.
col 3: education level: junior_college, university, senior_high_school, technical_secondary_school.
col 4: artExperience：beginner, competent, proficient, expert
col 5: photographyExperience: beginner, competent, proficient, expert
col 6-10: Big-Five personality traits score.
```

###Annotation Explanation of GIAA

```
Note that PIAA annotation in PARA can also be transferred into "image-aesthetic score distribution" pair for training GIAA, since each image's aesthetic score is annotated by multiple annotators as well. 
The GIAA annotation files include: PARA-GiaaTrain.csv and PARA-GiaaTest.csv.

col 0: imageName.
col 1: session ID.
col 2: scene category.
col 3-11: aesthetics score distribution.
col 12-13: mean and std of image aesthetic score.
col 14-15: mean and std of image quality score.
col 16-22: composition score.
col 23-29: color score.
col 30-36: depth-of-field score.
col 37-43: light score.
col 44-57: content score.
col 58-64: willingness to share score.
col 65-72: emotion label distribution.
col 73-77: difficulty of judgement. -1, 0, 1 represent easy, normal, difficult respectively.
col 78-79: is_object_emphasis, 0 equals to false and 1 equals to True.
col 80-81: mean and std of is_object_emphasis.
col 82-86: score of Big-Five personality traits.
col 87-90: photography experience classification label of all annotators.
col 91-94: art experience classification label of all annotators.
```
## Reference

---

If you find our work useful, please cite this work. Thank you.

## License

---

1. Dataset Website  
OPPO Research Institute Public Data is a dataset website ("Site") operated by Guangdong OPPO Mobile Telecommunications Corp. Ltd. and/or its affiliates ("OPPO" or "we"), consisting of papers and related datasets. This Service Agreement on [Dataset Website] and other policies, rules, announcements, hyper-links, notices, FAQs published on the Site (collectively, the "Agreement") are agreements between you and the Site with respect to, among other things, your access to and use of the Site. 
You click to confirm or download dataset through the Site or otherwise choose to accept this Agreement. If you do not accept this Agreement, please do not use the Site or download relevant dataset. 
In order to better provide you with service, please be sure to read carefully and fully understand all terms and conditions before you access and use the Site, especially the exclusion or limitation of liability, license of rights and use of information, legal application and dispute resolution. The restrictions or disclaimers will remind you to pay attention by bold or underlined form. 

2. Specification for Use  
Any materials and data downloaded from the Site can only be used for research and learning purpose. You are not allowed to sell, transfer or use in any commercial activities any dataset or any research results or outputs based on datasets obtained from the Site. 
If you use any dataset on the Site in any public place, for instance to publish papers or public speeches, you must specify the sources. 
Please use the Site and datasets provided on the Site based on the terms agreed in the Service Agreement, in compliance with the law and regulations, in line with the social public order and good morals, and in no way infringing upon legitimate rights and interests of any third party. 

3. Intellectual Property  
All content of the Site, including without limitation text, videos, images, datasets, programs, Mark and other materials and services which are protected by copyright and other intellectual property rights laws, are owned by OPPO and/or its authorized third parties, or used by OPPO under legal authorization. 

4. Disclaimer  
THE DATABASE PROVIDED HEREUNDER IS PROVIDED "AS IS" AND OPPO MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION WARRANTIES OF ACCURACY, COMPLETENESS, LEGALITY, NON-INFRINGEMENT, FITNESS, MERCHANTABILITY FOR A PARTICULAR PURPOSE. OPPO shall have no obligation to maintain, support, update, enhance or modify the content of the Data. You shall be solely responsible for, and shall defend OPPO from any and all claims arising from your use of the Data. In no event shall OPPO be liable to either party for any direct, indirect, special, incidental, punitive, incidental or consequential damages arising from the use of the Data Site or its documentation, even if OPPO has been advised of the possibility of such damages. 

5. Updating of Site and Database  
In consideration of the unique nature of the services provided on the Site, you agree that OPPO may add, delete, modify, upgrade, transfer, suspend or terminate the OPPO and the related database service at any time at OPPO's sole discretion. 

6. Governing Law and Dispute Resolution  
The validity, interpretation, modification, performance and dispute resolution of this Agreement shall be governed by the laws of the Mainland of People's Republic of China, excluding any conflict of law rules. 
If any dispute arises in connection with the execution, performance or interpretation of this Agreement between OPPO and you, the parties shall use their best efforts to resolve such dispute amicably through consultation. If such consultation fails, OPPO and you agree to submit such dispute to Shenzhen Court of International Arbitration for arbitration. 




