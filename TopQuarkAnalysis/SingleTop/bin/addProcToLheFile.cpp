// g++ -Wall -o addProcToLheFile addProcToLheFile.cpp

#include <iostream>
#include <fstream>



int main(int argc, char** argv)
{
  if(argc != 3)
  {
    std::cout << ">>>addProcToLheFile.cpp::Usage:   " << argv[0] << "   initialFile.lhe   IPROC" << std::endl;
    return -1;
  }
  
  char* initialFileName = argv[1]; 
  char* IPROC = argv[2]; 
  
  std::cout << "initialFileName = " << initialFileName << std::endl;
  std::cout << "IPROC = " << IPROC << std::endl;
  
  
  
  // open lhe file
  std::ifstream initialFile(initialFileName, std::ios::in);
  std::ofstream outFile("out.lhe", std::ios::out);
  
  std::string line;
  
  while(!initialFile.eof())
  {
    getline(initialFile, line);
    
    if( line == "<!--" )
    {
      outFile << "<header>" << std::endl;
      outFile << "<herwig6header>" << std::endl;
      outFile << "IPROC = " << IPROC << std::endl;
      outFile << "</herwig6header>" << std::endl;
      outFile << "</header>" << std::endl;
    } 
    
    outFile << line << std::endl;
  }
  
  
  return 0;
}
