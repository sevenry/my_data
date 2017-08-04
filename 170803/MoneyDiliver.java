package com.tech.sry4;

import java.awt.font.NumericShaper.Range;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CountDownLatch;

public class MoneyDiliver {
    
    public static void main(String [] args){
        MoneyDiliver a = new MoneyDiliver();
        MoneyDiliver b = new MoneyDiliver();
        MoneyDiliver c = new MoneyDiliver();
        MoneyDiliver d = new MoneyDiliver();
        MoneyDiliver e = new MoneyDiliver();
        MoneyDiliver f = new MoneyDiliver();
        
        int loopa = 1000;
        int loopb = 3000;
        int loopc = 10000;
        int loopd = 30000;
        int loope = 80000;
        int loopf = 200000;
        a.times_ans(loopa);
        b.times_ans(loopb);
        c.times_ans(loopc);
        d.times_ans(loopd);
        e.times_ans(loope);
        f.times_ans(loopf);
    }
    
    public void times_ans(int loop){
        int max_ave = 0;
        int min_ave = 0;
        int peopleCount = 0;
        for(int time = 0 ;time<10;time++){
            MoneyDiliver a = new MoneyDiliver();
            int [] abc = a.ans(loop);
            int max = 100;
            int min = 100;
            peopleCount+=abc.length;
            for(int i = 0;i<abc.length;i++){
                if (abc[i]<min){
                    min = abc[i];
                }
                if (abc[i]>max){
                    max=abc[i];
                }
            }
            max_ave+=max;
            min_ave+=min;
        }
        System.out.println(loop+"回合后最大值平均值：  "+max_ave/10);
        System.out.println(loop+"回合后最低值平均值：  "+min_ave/10);
        System.out.println(loop+"回合后平均还有"+peopleCount/10+"玩家");
    }
    
    public int[] delete(int []abc,int index){
        int lenth = abc.length-1;
        int [] newabc = new int[lenth];
        
        for(int i=0;i<index;i+=1){
            newabc[i]=abc[i];
        }
        for(int i=index;i<lenth;i+=1){
            newabc[i] = abc[i+1];
        }
        return newabc;
    }
    
    public int[] deleteZero(int []abc){
        int [] newabc = null;
        int k = 0;
        for(int i = 0; i <abc.length;i+=1){
            if(abc[i]==0){
                k=1;
                newabc=delete(abc, i);
                break;
            }
        }
        if(k==1){
            newabc = deleteZero(newabc);
        }
        else {
            newabc = abc;
        }
        //System.out.println(newabc.length+" here?");
        return newabc;
    }
   
    //给定一次试验的循环次数，输出当前所有玩家手中的钱数。
    public int[] ans(int loop){
        int[] abc = setInt();
        //循环次数
        int[] ansabc = null;
        int people = 100;
        for(int i=0;i<loop;i+=1){
            abc = aLoop(abc,people);
            abc = deleteZero(abc);
            //System.out.println(i+"  ok  "+abc.length);
            people = abc.length;
        }
        return abc;
    }
    
    public int[] setInt(){
        //初始值，一百个人，每人一百块
        int [] abc = new int[100];
        for (int i=0;i<100;i=i+1) {
            abc[i]=100;
        }
        return abc;
    }
    
    public int diliver(int i,int people) {
            
        Random random = new Random();

        int k = random.nextInt(people-1);
        if(k<i){
            return k;
        }
        else{
            return k+1;
        }
    }    
    
    public int[] aLoop (int[] aList,int people){
        //每人依次给钱。
        //System.out.println("whyh?"+people);
        for (int i=0;i<people; i=i+1){
            int k = diliver(i,people);
            //System.out.println(k+"maybe");
            int money=1;
            //修改游戏规则：选中玩家后，如果出钱方钱数高于5，则随机给一笔不高于5元的钱。
            if (aList[i]>5){
                Random a = new Random();
                money = a.nextInt(5)+1;
            }
            aList[i]-= money;
            aList[k]+=money;
                
        }
        //System.out.println(aList[0]);
        return aList;
    }


}