#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node{
    int data;
    struct node *next;
};

typedef struct node Data;

Data* newnode(int data){
    Data* temp = (Data*)malloc(sizeof(Data));
    temp -> data = data;
    temp -> next = NULL;
    return temp;
}

void add(Data* head,int data){
    Data* head =NULL;
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

Data* searchnode(Data* head,int target){
    Data* head =NULL;
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

void insert(Data* head,int target,int data){
    Data* head = NULL;
    Data* node1;
    Data* node2 = (Data*)malloc(sizeof(Data));
    if(searchnode(head,target) != NULL){
        printf("INSERT_SUCC\n");
        node1 = searchnode(head,target);
        node2 -> next = node1 -> next;
        node1 -> next = node2;
        node2 -> data = target;
        node1 -> data = data;
    }
    else{
        printf("INSERT_FAIL\n");
    }
}

void search(Data* head,int target){
    Data* head = NULL;
    if(searchnode(head,target) != NULL){
        printf("FOUND\n");
    }
    else{
        printf("NOT FOUND\n");
    }
}

void update(Data* head,int target,int data){
    Data* head = NULL;
    Data* node=(Data*)malloc(sizeof(Data));
    if(searchnode(head,target) != NULL){
        printf("UPDATE_SUCC\n");
        node=searchnode(head,target);
        node -> data = data;
    }
    else{
        printf("UPDATE_FAIL\n");
    }
}

void delete(Data* head,int target){
    Data* head = NULL;
    Data* temp,* node;
    temp = head;
    node = searchnode(head,target);
    if(head == NULL){
        printf("DELETE_FAIL\n");
    }
    else if(head -> data == target){
        head = head -> next;
        free(temp);
        printf("DELETE_SUCC\n");
    }
    else if(node == NULL){
        printf("DELETE_FAIL\n");
    }
    else{
        while(temp -> next != node){
            temp = temp -> next;
        }
        temp -> next = node -> next;
        free(node);
        printf("DELETE_SUCC\n");
    }
}

void print1(Data* start){
    while(start -> next != NULL){
        printf("%d ",start->data);
        start = start-> next;
    }
    printf("%d\n",start -> data);
}

void printall(Data* head){
    Data* head = NULL;
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
    Data* head;
    while(scanf("%s",a) != EOF){
        if(strcmp(a,"print")==0){
            printall(head);
        }
        else if(strcmp(a,"add")==0){
            scanf("%d",&data);
            add(head,data);
            printf("ADD_SUCC\n");
        }
        else if(strcmp(a,"insert")==0){
            scanf("%d %d",&target,&data);
            insert(head,target,data);
        }
        else if(strcmp(a,"search")==0){
            scanf("%d",&target);
            search(head,target);
        }
        else if(strcmp(a,"update")==0){
            scanf("%d %d",&target,&data);
            update(head,target,data);
        }
        else if(strcmp(a,"delete")==0){
            scanf("%d",&target);
            delete(head,target);
        }
    }
    return 0;
}