//函式大原則，有要更動的數值才用pointer
//不改就沒必要使用pointer傳，避免意外修改數值
//但陣列例外
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

#define finish          "\033[0m"
#define black           "\033[30m"
#define red             "\033[31m"
#define green           "\033[32m"
#define yellow          "\033[33m"
#define blue            "\033[34m"
#define purple          "\033[35m"
#define dark_green      "\033[36m"
#define white           "\033[37m"

int check_boundary(int ir, int ic, int mapr, int mapc);
int check_availability();
int check_move();
void setup_village();
void setup_monster();
void setup_player(char **map, int *pr, int *pc, int mapr, int mapc);
void go_up();
void go_down();
void go_right();
void go_left();
void print_map();
void clean_map();
void pre_work();
char **create_map();

int main(){
    int input;
    int mapr, mapc;
    int pr, pc;
    char **map = NULL;

    //建地圖
    pre_work(map, &mapr, &mapc);

    setup_player(map, &pr, &pc, mapr, mapc);
    print_map(map, mapr, mapc);

    while (1){
        printf("[W] go up [S] go down [D] go right [A] go left [P] exit: \n");
        input = getch();
        system("cls");
        system("cls");
        switch(input){
        case 'W':
        case 'w':
            go_up(map, &pr, pc, mapr, mapc);
            break;
        case 'S':
        case 's':
            go_down(map, &pr, pc, mapr, mapc);
            break;
        case 'D':
        case 'd':
            go_right(map, pr, &pc, mapr, mapc);
            break;
        case 'A':
        case 'a':
            go_left(map, pr, &pc, mapr, mapc);
            break;
        case 'P':
        case 'p':
            exit(0);
        default:
            printf("Invalid Choice\n");
            break;
        }
    }
    clean_map(map, mapr);
    return 0;
}
//檢查是否在地圖之內
int check_boundary(int ir, int ic, int mapr, int mapc){
    if ((ir >= 0 && ir < mapr) && (ic >= 0 && ic < mapc)){
        return 1;
    }
    printf("the location is outside the map\n");
    return 0;
}
//檢查格子是否有東西
int check_availability(char **map, int ir, int ic){
    if (map[ir][ic] == '.'){
        return 1;
    }
    printf("the location is occupied\n");
    return 0;
}

void pre_work(char **map,int *mapr,int *mapc){
    int input;
    while (1){
        map = create_map(map, &mapr, &mapc);
        setup_village(map, mapr, mapc);
        setup_monster(map, mapr, mapc);
        print_map(map, mapr, mapc);

        //詢問意見，2表示重建地圖，先清空
        printf("[1] Create a new map [2] Start travel the map: \n");
        scanf("%d", &input);
        if (input == 1){
            clean_map(map, mapr);
        }
        else{
            break;
        }
    }
}
//檢查移動(其實就是上面兩個函式)
int check_move(char **map, int ir, int ic, int mapr, int mapc){
    //滿足下面所有條件就會回傳1，否則回傳0
    return (ir >= 0 && ir < mapr && ic >= 0 && ic < mapc && map[ir][ic] == '.');
}
//設定村莊
void setup_village(char **map, int mapr, int mapc){
    int ir, ic;

    do{
        printf("Input the row and column for the village location:\n");
        scanf("%d %d", &ir, &ic);
        //因為 "!" check_boundary，所以超出地圖時就會回傳1，跑回while(快速邏輯運算)
        //如果在地圖內再進一步判斷格子上是否為'.'
    } while (!check_boundary(ir, ic, mapr, mapc) || !check_availability(map, ir, ic));
    map[ir][ic] = 'v';
}
//設定怪獸
void setup_monster(char **map, int mapr, int mapc){
    int ir, ic;
    int monster_amount = mapr / 10 + mapr % 10;

    printf("You need to assign location for %d monsters in total\n", monster_amount);
    for (int i = 0; i < monster_amount; i++){
        printf("Input the row and column for monster %d:\n", i);
        scanf("%d %d", &ir, &ic);
        if (!check_boundary(ir, ic, mapr, mapc) || !check_availability(map, ir, ic)){
            --i;
        }
        else{
            map[ir][ic] = 'm';
        }
    }
}
//設定玩家初始位
void setup_player(char **map, int *pr, int *pc, int mapr, int mapc){
    do{
        printf("Input the row and column for player:\n");
        //用pointer傳，所以不用加&
        scanf("%d %d", pr, pc);
    } while (!check_boundary(*pr, *pc, mapr, mapc) || !check_availability(map, *pr, *pc));
    map[*pr][*pc] = 'p';
}
//各種走路
void go_up(char **map, int *pr, int pc, int mapr, int mapc){
    if (!check_move(map, *pr-1, pc, mapr, mapc)){
        printf("You can't go there\n");
        return;
    }
    map[*pr][pc] = '.';
    *pr -= 1;
    map[*pr][pc] = 'p';
    print_map(map,mapr,mapc);
}

void go_down(char **map, int *pr, int pc, int mapr, int mapc){
    if (!check_move(map, *pr+1, pc, mapr, mapc)){
        printf("You can't go there\n");
        return;
    }
    map[*pr][pc] = '.';
    *pr += 1;
    map[*pr][pc] = 'p';
    print_map(map,mapr,mapc);
}

void go_left(char **map, int pr, int *pc, int mapr, int mapc){
    if (!check_move(map, pr, *pc-1, mapr, mapc)){
        printf("You can't go there\n");
        return;
    }
    map[pr][*pc] = '.';
    *pc -= 1;
    map[pr][*pc] = 'p';
    print_map(map,mapr,mapc);
}

void go_right(char **map, int pr, int *pc, int mapr, int mapc){
    if (!check_move(map, pr, *pc+1, mapr, mapc)){
        printf("You can't go there\n");
        return;
    }
    map[pr][*pc] = '.';
    *pc += 1;
    map[pr][*pc] = 'p';
    print_map(map,mapr,mapc);
}
//印地圖
void print_map(char **map, int mapr, int mapc){
    printf(purple"==== MAP ====\n");
    for (int i = 0; i < mapr; i++){
        for (int j = 0; j < mapc; j++){
            if(map[i][j]=='.'){
                printf(green"%c ", map[i][j]);
            }
            else if(map[i][j]=='v'){
                printf(yellow"%c ", map[i][j]);
            }
            else if(map[i][j]=='m'){
                printf(blue"%c ", map[i][j]);
            }
            else if(map[i][j]=='p'){
                printf(red"%c ", map[i][j]);
            }
        }
        printf("\n");
    }
    printf(purple"==== MAP ====\n"finish);
}
//指標不用要清空，避免浪費記憶體
void clean_map(char **map, int mapr){
    //先對每個一維指標清空
    for (int i = 0; i < mapr; i++)
        free(map[i]);
    //再對其餘清空
    //特別注意如果先清空map，就會找不到每一個map[i]，就無法清空
    //所以要先清空一維的map[i]，再清map
    free(map);
}
//創地圖
char **create_map(char **map, int *mapr, int *mapc){
    //輸入行列數值
    printf("Input the number of row and column for the map:\n");
    scanf("%d %d", mapr, mapc);
    //先為二維指標開空間(存放一維指標)
    map = (char **)malloc(sizeof(char *) * (*mapr));
    //再對一維指標開空間(放真正的數值)
    for (int i = 0; i < (*mapr); i++){
        map[i] = (char *)malloc(sizeof(char) * (*mapc));
        memset(map[i], '.', *mapc);
    }
    return map;
}