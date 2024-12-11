import java.io.*;
import java.util.*;
import java.lang.Math;
import java.math.BigInteger;

class Day11Part2{

   public static final String INPUT_FILE = "data/day23input.txt";
   


   public static void main(String[] args) throws Exception{
   
      ArrayList<BigInteger> stones = buildStones();
      ArrayList<Thread> threads = new ArrayList<>();
      
      displayStones(stones);
      
      for (int i = 0; i < stones.size(); i++){
         MyRunnable runnable = new MyRunnable();
         runnable.setStart(stones.get(i));
         Thread thread = new Thread(runnable);
         thread.start();
         threads.add(thread);
      }

   }
 
   public static ArrayList<BigInteger> buildStones() throws Exception{
      BufferedReader br = new BufferedReader(new FileReader(new File("data/day11.txt")));
      String[] parts = br.readLine().split(" ");
      ArrayList<BigInteger> numbers = new ArrayList<BigInteger>();
      
      for (int i = 0; i < parts.length; i++){
         numbers.add(new BigInteger(parts[i]));
      }
      return numbers;
   }  
   
   public static int getDigitCount(BigInteger number){
      int count = 0;
      while (number.compareTo(BigInteger.ZERO)>0){
         count++;
         number = number.divide(BigInteger.TEN);
      }
      return count;
   }
   
   public static void displayStones(ArrayList<BigInteger> numbers){
      
      
      for (int i = 0; i < numbers.size(); i++){
         System.out.print(numbers.get(i));
         System.out.print(",");
      }
      System.out.println();
   }
}

class Total {
   private static long total = 0;
   private static int finished = 0;
   public static synchronized void add(long amount){
      total += amount;
      finished++;
      System.out.printf("Finished threads: %s Current total: %s\n",finished,total);
   }
   public static long getTotal(){
      return total;
   }
}

class MyRunnable implements Runnable{
   private BigInteger start;
   public void run() {
      System.out.println(Thread.currentThread().getName() + ", executing run() method!");
      BigInteger product = BigInteger.valueOf(2024);
      
      ArrayList<BigInteger> stones = new ArrayList<BigInteger>();
      
      
      while (start == null){
         try {
            Thread.sleep(1000); // 1000 milliseconds = 1 second
         } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Restore interrupted status
         }
      }
      
      
      stones.add(start);
      
      
      for (int j = 0; j<75;j++){
         int i = 0;
         while (i<stones.size()){
            BigInteger stone = stones.get(i);
            int stone_digits = Day11Part2.getDigitCount(stone);
            if (stone.compareTo(BigInteger.ZERO)==0){
               stones.set(i,BigInteger.valueOf(1));
            }else if (stone_digits%2==0){
               //System.out.print(stone);
               BigInteger power = BigInteger.TEN.pow(stone_digits/2);
               stones.set(i,stone.divide(power));
               i++;
               stones.add(i,stone.mod(power));
               //System.out.print(stones.get(i-1));
               //System.out.println(stones.get(i));
               
            }else{
               stones.set(i,stone.multiply(product));
            }
            i++;
            //displayStones(stones);
         }
         System.out.printf("%s %s:%s\n",start,j,stones.size());
      }
      
      Total.add(stones.size());
   }
   
   public synchronized void setStart(BigInteger stone){
      start = stone;
   }
   public BigInteger getStart(){
      return start;
   }
}