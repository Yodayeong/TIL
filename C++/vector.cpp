//vector 컨테이너란?

//자동으로 메모리가 할당되는 배열.

//vector의 생성자

//vector<int> v; - 비어있는 vecor v를 생성
//vector<int> v(5); - 기본값(0)으로 초기화 된 5개의 원소를 가지는 vector v를 생성
//vector<int> v(5, 2); - 2로 초기화 된 5개의 원소를 가지는 vector v를 생성
//vector<int> v2(v1); - v2는 v1 vector를 복사해서 생상됨

//vector의 멤버 함수

//v.assign(5, 2); - 2의 값으로 5개의 원소 할당
//v.at(idx); - idx번째 원소를 참조함
//v[idx]; - idx번째 원소를 참조함. v.at(idx)보다 빠름
//v.front(); - 첫번째 원소를 참조함
//v.back(); - 마지막 원소를 참조함
//v.clear(); - 모든 원소를 제거함(원소만 제거하고 메모리는 남아있음)
//v.push_back(7); - 마지막 원소 뒤에 원소 7일 삽입함
//v.pop_back(); - 마지막 원소를 제거함
//v.insert(2, 3); - 2번째 위치에 3의 값을 삽입함
//v.size(); - 원소의 갯수를 리턴함
//v.capacity(); - 할당된 공간의 크기를 리턴함

#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    vector<int> v;

    cout << "[ v[i], v.size(), v.capacity() ]" << endl;
    for(int i = 0; i <= 64; i++) {
        v.push_back(i+1);
        cout << "[" << v[i] << "," << v.size() << "," << v.capacity() << "]" << endl;
    }

    for(int i = 0; i <= v.size()-1; i++) {
        cout << v[i] << endl;
    }

    return 0;
}