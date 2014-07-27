Test_Data = read.table(file="X_test.txt",sep="")
Train_Data = read.table(file="X_train.txt",sep="")
Train_Act = read.table(file="y_train.txt",sep="")
Test_Act = read.table(file="y_test.txt",sep="")
attribute_names = read.table(file="features.txt",sep="")
Train_Sub = read.table(file="subject_train.txt",sep="")
Test_Sub = read.table(file="subject_test.txt",sep="")


colnames(Test_Data) = attribute_names$V2
colnames(Train_Data) = attribute_names$V2

Test_Act$V1 <- gsub("4","SITTING",Test_Act$V1)
Test_Act$V1 <- gsub("3","WALKING_DOWNSTAIRS",Test_Act$V1)
Test_Act$V1 <- gsub("2","WALKING_UPSTAIRS",Test_Act$V1)
Test_Act$V1 <- gsub("1","WALKING",Test_Act$V1)
Test_Act$V1 <- gsub("6","LAYING",Test_Act$V1)
Test_Act$V1 <- gsub("5","STANDING",Test_Act$V1)

Train_Act$V1 <- gsub("4","SITTING",Train_Act$V1)
Train_Act$V1 <- gsub("3","WALKING_DOWNSTAIRS",Train_Act$V1)
Train_Act$V1 <- gsub("2","WALKING_UPSTAIRS",Train_Act$V1)
Train_Act$V1 <- gsub("1","WALKING",Train_Act$V1)
Train_Act$V1 <- gsub("6","LAYING",Train_Act$V1)
Train_Act$V1 <- gsub("5","STANDING",Train_Act$V1)


Train_Data = cbind(Train_Data,Train_Act)
Test_Data = cbind(Test_Data,Test_Act)

names(Train_Data$V1)[562] = "Activties"
names(Test_Data$V1)[562] = "Activties"

Train_Data = cbind(Train_Data,Train_Sub)
Test_Data = cbind(Test_Data,Test_Sub)

Merge_Data = rbind(Train_Data,Test_Data)
names(Merge_Data)[563] = "Subject"
names(Merge_Data)[562] = "Activities"


Merge_Data_Me = Merge_Data[,grep(pattern="mean",names(Merge_Data))]
Merge_Data_Sd = Merge_Data[,grep(pattern="std",names(Merge_Data))]
Merge_Data_Me_Sd = cbind(Merge_Data_Me,Merge_Data_Sd)

Merge_Data_Me_Sd = cbind(Merge_Data_Me_Sd,Merge_Data$Activities)
Merge_Data_Me_Sd = cbind(Merge_Data_Me_Sd,Merge_Data$Subject)

names(Merge_Data_Me_Sd)[80]  <- "Activities"
names(Merge_Data_Me_Sd)[81]  <- "Subject"


Final_Tidy_Data = aggregate( . ~ Activities + Subject, data = Merge_Data_Me_Sd,FUN=mean)

View(Final_Tidy_Data)

write.table(x=Final_Tidy_Data, "Final_Data_Set.txt",row.names=TRUE)
