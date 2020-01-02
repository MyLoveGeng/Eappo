#include<iostream>
using namespace std;

class DynamicArray{
	private:
		int *ptr;
		int size;
		
	public:
		DynamicArray():size(0){
			//构造函数构建初始化数组 
			ptr = NULL;
			cout<<"数组初始化成功！"<<endl; 
		}
	
		~DynamicArray(){
			//释放数组 
			if(ptr){
				delete[] ptr;
				cout<<"数组释放成功！"<<endl; 
			}	
		}
		
			
		void add_elem(int elem){
			//尾入法插入一个元素 
			if(ptr){
				int *tmptr = new int[size+1];
				memcpy(tmptr, ptr, sizeof(int)*size);
				delete[] ptr;
				ptr = tmptr;
			}else{
				ptr = new int[1];
			}
			ptr[size++] = elem;
		}
		
		void fun(int n){
			//实现写入5或7的倍数
			for(int i=2; i<=n; i++){
				if(i%5==0||i%7==0)
					add_elem(i);
			}
		}

		void show(){
			//打印数组 
			for(int i=0; i<size	; i++){
				cout<<ptr[i]<<'\t';
			}
			cout<<endl;
		}	
};

int main(){
	DynamicArray da;
	da.fun(100);
	da.show();
}
