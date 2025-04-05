#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

class Book{
public:
    string title;
    string author;
    string id;
    bool isissued;

    Book(string title,string author,string id){
        this->title=title;
        this->author=author;
        this->id=id;
        isissued=false;
    }
    Book(string title,string author,string id,bool issued){
        this->title=title;
        this->author=author;
        this->id=id;
        this->isissued=issued;
    }
    void display(){
        cout<<"Book ID : "<<id<<"  "<<"Title : "<<title<<"  "<<"Author : "<<author<<"  "<<"Issued : "<<(isissued?"Yes":"No")<<'\n';
    }
};
class Member{
public:
    string name;
    string memberid;
    Member(string name,string id){
        this->name=name;
        memberid=id;
    }
    void display(){
        cout<<"Member ID : "<<memberid<<"  "<<"Member Name : "<<name<<'\n';
    }
};
class librarian{
private:
    string name;
public:
    vector<Book> books;
    vector<Member> members;

    librarian(string name){
      this->name=name;
      loadbooks();
      loadmembers();
   }

   void savebooks(){
      ofstream file("books.txt");
      for(auto &book:books){
         file<<book.id<<","<<book.title<<","<<book.author<<","<<book.isissued<<'\n';
      }
      file.close();
   }
   void loadbooks(){
      ifstream file("books.txt");
      if(!file) return;
      books.clear();
      string id,title,author,issuedStr;
      while(getline(file,id,',')&&
      getline(file,title,',')&&
      getline(file,author,',')&&
      getline(file,issuedStr)){
         books.push_back(Book(title,author,id,issuedStr=="1"));
      }
   }
   void savemembers(){
      ofstream file("members.txt");
      for(auto &member:members){
         file<<member.memberid<<","<<member.name<<'\n';
      }
      file.close();
   }
   void loadmembers(){
      ifstream file("members.txt");
      if(!file) return;
      members.clear();
      string id,name;
      while(getline(file,id,',')&&getline(file,name)){
         members.push_back(Member(name,id));
      }
      file.close();
   }


    void addbook(string title,string author,string id){
       books.push_back(Book(title,author,id));
       savebooks();
       cout<<"Book Added : "<<title<<'\n';
    }
    void addmember(string name,string id){
        members.push_back(Member(name,id));
        savemembers();
        cout<<"Member Added : "<<name<<'\n';
    }
    void issuebook(string bookid){
        for(auto &book:books){
            if(book.id==bookid && !book.isissued){
                book.isissued=true;
                savebooks();
                cout<<"Book issued "<<book.title<<'\n';
            }
        }
        cout<<"Book is not available at moment."<<"\n";
    }
    void returnbook(string bookid){
        for(auto &book : books){
            if (book.id==bookid&&book.isissued){
                book.isissued=false;
                savebooks();
                cout<<"Book returned : "<<book.title<<'\n';
            }
        }
        cout<<"Book not found.\n";
    }
    void displayBooks(){
        cout<<"\nLibrary Books : \n";
        for(auto &book:books){
            book.display();
        }
    }
    void displaymembers(){
        cout<<"\nRegistered Members : \n";
        for(auto &member:members){
            member.display();
        }
    }
};

int main(){
    bool running=true;
    string name;
    cout<<"Give Your name : ";
    cin>>name;
    librarian Librarian(name);
    while(running){
    int choice;

    cout<<"Hello "<<name<<" enter your choice :\n"; 
    cout<<"1.Display Books \n";
    cout<<"2.Display members \n";
    cout<<"3.Add book \n";
    cout<<"4.Add Member \n";
    cout<<"5.Issue Book\n";
    cout<<"6.Return Book\n";
    cout<<"7.EXIT       \n";
    cin>>choice;
    if(choice==1){
        Librarian.displayBooks();
    }
    else if(choice==2){
        Librarian.displaymembers();
    }
    else if(choice==3){
        string t;
        string a;
        string i;
        cout<<"Give Title of Book : \n";
        cin>>t;
        cout<<"Give name of author : \n";
        cin>>a;
        cout<<"Give id of book : \n";
        cin>>i;
        Librarian.addbook(t,a,i);
    }
    else if(choice==4){
        string n;
        string i;
        cout<<"Give name of member : \n";
        cin>>n;
        cout<<"Give id of member : \n";
        cin>>i;
        Librarian.addmember(n,i);
    }
    else if(choice==5){
        string i;
        cout<<"Give id of book : \n";
        cin>>i;
        Librarian.issuebook(i);
    }
    else if(choice==6){
        string i;
        cout<<"Give id of book : \n";
        cin>>i;
        Librarian.returnbook(i);
    }
    else if(choice==7){
        running=false;
    }
}

    return 0;
}