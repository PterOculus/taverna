package org.example;

public class ThreadHW {
    private static final int SIZE = 10_000_000;
    private static final int HALF = SIZE/2;

    public static void withoutConcurrency() {
        float[] arr = new float[SIZE];
        for (int i = 0; i < SIZE; i++) {
            arr[i] = 1f;
        }
        long before = System.currentTimeMillis();
        for (int i = 0; i < SIZE; i++) {
            float f = (float) i;
            arr[i]= (float) (arr[i] * Math.sin(0.2f + f/5) * Math.cos(0.2f + f/5) * Math.cos(0.4f + f/2));
        }
        long after = System.currentTimeMillis();
        System.out.printf("without : %s\n",after - before);
    }
    public static void withConcurrancy() {
        float[] arr1 = new float[SIZE];
        for (int i = 0; i < SIZE; i++) {
            arr1[i] = 1f;
        }

        long before1 = System.currentTimeMillis();
        float[] arr2 = new float[HALF];
        float[] arr3 = new float[HALF];
        float[] arrR = new float[SIZE];
        System.arraycopy(arr1,0,arr2,0,HALF);
        System.arraycopy(arr1,HALF,arr3,0,HALF);
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < HALF; i++) {
                    float f = (float) i;
                    arr2[i]= (float) (arr2[i] * Math.sin(0.2f + f/5) * Math.cos(0.2f + f/5) * Math.cos(0.4f + f/2));
                }
            }
        });
        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < HALF; i++) {
                    float f = (float) i;
                    arr3[i]= (float) (arr3[i] * Math.sin(0.2f + f/5) * Math.cos(0.2f + f/5) * Math.cos(0.4f + f/2));
                }
            }
        });
        thread.start();
        thread2.start();
        try {
            thread.join();
            thread2.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.arraycopy(arr2, 0,arr1,0,HALF);
        System.arraycopy(arr3,0,arr1,HALF,HALF);

        long after1 = System.currentTimeMillis();
        System.out.printf("with : %s\n",after1 - before1);
    }
}
