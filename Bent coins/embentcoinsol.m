% Exercise on EM
% Author: Pratik Shah
% Date: February 21, 2020
% 
% Ten bent coins, Unknown Biases, Equally likely to get selected for tossing
% Given T observation sequences 
% Parameter learning using Expectation maximization
%
% Reference: What is expectation maximization algorithm? Chuong B Do and Serafim Batzoglou, Nature Biotechnology, Vol 26, Num 8, Aug 2008

clear all;
close all;

%y=csvread("two_bent_coins.csv");
y=csvread("two_bent_coins.csv");

% True Parameters
% theta = [.2 .5];

theta = [.2 .5];

h = sum(y,2); t = 20-h;
th(1,:) = theta;

for n=2:10
 LH=zeros(size(h));
 for k=1:2
  lh(:,k) = (th(n-1,k).^h).*((1-th(n-1,k)).^t);
  LH=LH+lh(:,k);
 end
 for k=1:2
  th(n,k)=sum(h.*lh(:,k)./LH)/sum((h+t).*lh(:,k)./LH);
 end
end

