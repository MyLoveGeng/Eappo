#include<iostream>
using namespace std;

class DynamicArray{
	private:
		int *ptr;
		int size;
		
	public:
		DynamicArray():size(0){
			//���캯��������ʼ������ 
			ptr = NULL;
			cout<<"�����ʼ���ɹ���"<<endl; 
		}
	
		~DynamicArray(){
			//�ͷ����� 
			if(ptr){
				delete[] ptr;
				cout<<"�����ͷųɹ���"<<endl; 
			}	
		}
		
			
		void add_elem(int elem){
			//β�뷨����һ��Ԫ�� 
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
			//ʵ��д��5��7�ı���
			for(int i=2; i<=n; i++){
				if(i%5==0||i%7==0)
					add_elem(i);
			}
		}

		void show(){
			//��ӡ���� 
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
