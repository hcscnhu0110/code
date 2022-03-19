#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node{
    int data;
    int target;
    struct node *next;
};

typedef struct node Data;

Data* head =NULL;
Data* newnode(int data){
    Data* temp = (Data*)malloc(sizeof(Data));
    temp -> data = data;
    temp -> next = NULL;
    return temp;
}

void add(int data){
    Data* temp = head;
    if(head == NULL){
        head = newnode(data);
    }
    else{
        while(temp -> next != NULL){
            temp = temp -> next;
        }
        temp -> next = newnode(data);
    }
}

Data* searchnode(int target){
    Data* node = head;
    while(node != NULL){
        if(node -> data == target){
            return node;
        }
        else{
            node = node -> next;
        }
    }
    return NULL;
}

void insert(int target,int data){
    Data* node1;
    Data* node2 = (Data*)malloc(sizeof(Data));
    if(searchnode(target) != NULL){
        printf("INSERT_SUCC\n");
        node1 = searchnode(target);
        node2 -> next = node1 -> next;
        node1 -> next = node2;
        node2 -> data = target;
        node1 -> data = data;
    }
    else{
        printf("INSERT_FAIL\n");
    }
}

void search(int target){
    if(searchnode(target) != NULL){
        printf("FOUND\n");
    }
    else{
        printf("NOT FOUND\n");
    }
}

void update(int target,int data){
    Data* node=(Data*)malloc(sizeof(Data));
    if(searchnode(target) != NULL){
        printf("UPDATE_SUCC\n");
        node=searchnode(target);
        node -> data = data;
    }
    else{
        printf("UPDATE_FAIL\n");
    }
}

void delete(int target){
    Data* temp,* follow;
    temp = head;
    if(head == NULL){
        printf("DELETE_FAIL\n");
    }
    if(head -> data == target){
        printf("DELETE_SUCC\n");
        head = head -> next;
        free(temp);
    }
    while((temp != NULL) && (temp -> data != target)){
        follow = temp;
        temp = temp -> next; 
    }
    if(temp == NULL){
        printf("DELETE_FAIL\n");
    }
    else{
        printf("DELETE_SUCC\n");
        follow -> next = temp -> next;
        free(temp);
    }
}

void print1(Data* start){
    while(start -> next != NULL){
        printf("%d ",start->data);
        start = start-> next;
    }
    printf("%d\n",start -> data);
}

void printall(){
    if(head == NULL){
        printf(" \n");
    }
    else{
        print1(head);
    }
}

int main(){
    char a[100];
    int data;
    int target;
    while(scanf("%s",a) != EOF){
        if(strcmp(a,"print")==0){
            printall();
        }
        else if(strcmp(a,"add")==0){
            scanf("%d",&data);
            add(data);
            printf("ADD_SUCC\n");
        }
        else if(strcmp(a,"insert")==0){
            scanf("%d %d",&target,&data);
            insert(target,data);
        }
        else if(strcmp(a,"search")==0){
            scanf("%d",&target);
            search(target);
        }
        else if(strcmp(a,"update")==0){
            scanf("%d %d",&target,&data);
            update(target,data);
        }
        else if(strcmp(a,"delete")==0){
            scanf("%d",&target);
            delete(target);
        }
    }
}