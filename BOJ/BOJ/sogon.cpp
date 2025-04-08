#include <iostream>
#include <cstring>


using namespace std;

class Transportation {
protected:
	char companyName[10]; // 회사 이름
public:
	virtual char* getCompanyName() const = 0;
	virtual int getFare() const = 0;
};


class Taxi : public Transportation
{
private:
	// char companyName[10]; // 택시회사 이름
	int totalDistance; // 총 운행거리
public:
	Taxi(const char* companyName, int totalDistance);
	virtual char* getCompanyName() const override;
	virtual int getFare() const override; // 총 운행거리와 단위거리 당 요금(1000원 고정)의 곱을 반환함
};

Taxi::Taxi(const char* companyName, int totalDistance) {
	strcpy(this->companyName, companyName);
	this->totalDistance = totalDistance;
}

char* Taxi::getCompanyName() const {
	return (char*)companyName;
}

int Taxi::getFare() const {
	return totalDistance * 1000;
}


class Bus :public Transportation
{
private:
	// char companyName[10]; // 버스회사 이름
	int numBoarding; // 탑승 회수
public:
	Bus(const char* companyName, int numBoarding);
	virtual char* getCompanyName() const override;
	virtual int getFare() const override; // 탑승회수와 기본요금(1500원 고정)의 곱을 반환함
};

Bus::Bus(const char* companyName, int numBoarding) {
	strcpy(this->companyName, companyName);
	this->numBoarding = numBoarding;
}


char* Bus::getCompanyName() const {
	return (char*)companyName;
}

int Bus::getFare() const {
	return numBoarding * 1500;
}



class CreditCardCompany
{
private:
	int numTransportations;
	Transportation* transportationList[1000];
public:
	CreditCardCompany() : numTransportations(0) {};
	~CreditCardCompany()
	{
		for (int i = 0; i < numTransportations; i++)
			delete transportationList[i];
	}

	void addTransportation(Transportation* transportation);
	int getTotalFare();
};

void CreditCardCompany::addTransportation(Transportation* transportation) {
	transportationList[numTransportations] = transportation;
	numTransportations++;
}

int CreditCardCompany::getTotalFare()
{
	int res = 0;
	for (int i = 0; i < numTransportations; i++) {
		res += transportationList[i]->getFare();
	}
	return res;
}
class TransportationManager {
public:
	void addTansportations();
};

void TransportationManager::addTansportations()
{
	CreditCardCompany* pCreditCardCompany = new CreditCardCompany;
	Transportation* pNewTransportation = NULL;
	// 대중교통 이용내역 추가
	pNewTransportation = new Taxi("Hongik Taxi", 1200);
	pCreditCardCompany->addTransportation(pNewTransportation);
	pNewTransportation = new Taxi("Sangsu Taxi", 2300);
	pCreditCardCompany->addTransportation(pNewTransportation);
	pNewTransportation = new Bus("Seogyo Bus", 130);
	pCreditCardCompany->addTransportation(pNewTransportation);
	pNewTransportation = new Bus("Donggyo Bus", 220);
	pCreditCardCompany->addTransportation(pNewTransportation);
	// 통계 출력
	cout << "Total transportation fare is : " << pCreditCardCompany->getTotalFare() << endl;
}
int main(void) {


	TransportationManager tm;
	tm.addTansportations();

	return 0;
}


