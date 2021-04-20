library(bnlearn)

course.grades<-read.table("2020_course_grades.txt",head=TRUE)
course.grades.net<-hc(course.grades,"k2")
course.grades.net.fit<-bn.fit(course.grades.net, course.grades)
plot(course.grades.net)
