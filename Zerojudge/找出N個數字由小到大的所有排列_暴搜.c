#include <stdio.h>

void next(int size, int pivot, int perm[]){
    int i, collision;
    static int count=0;

    perm[pivot] = 0;
    while (perm[pivot] < size){
        perm[pivot]+=1;
    	collision = 0;
    	for (i=0; i<pivot; i++){
    	    if (perm[pivot] == perm[i]){
    	        collision = 1;
    	        break;
    	    }
        }
    	if (!collision){
            if (pivot+1 < size)
                next(size, pivot+1, perm);
            else{
            	printf("%4d: ", ++count);
                for (i=0; i<size; i++){
                    printf("%d ", perm[i]);
                }
                printf("%d ",pivot);
                printf("\n");
            }
        }
    }
}

void main()
{
    int size, perm[12] = {0};
    printf("Please input number of elements: ");
    scanf("%d", &size);
    next(size, 0, perm);
}