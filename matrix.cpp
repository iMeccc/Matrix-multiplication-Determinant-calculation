# include<iostream>
# include<vector>

class Matrix{
private:
    int row;
    int col;
    std::vector<std::vector<float>> m_matrix;

public:
    // zero constructor
    Matrix(): row(0), col(0){}
    Matrix(const int row, const int col): row(row), col(col), m_matrix(row, std::vector<float>(col, 0.0)){}
    // vector, copy, move constructor
    Matrix(const std::vector<std::vector<float>>& matrix): row(matrix.size()), col(matrix.empty() ? 0 : matrix[0].size()){
        m_matrix = matrix;
    }
    Matrix(const Matrix& matrix): row(matrix.row), col(matrix.col), m_matrix(matrix.m_matrix){}
    Matrix(Matrix&& matrix) noexcept: row(matrix.row), col(matrix.col), m_matrix(std::move(matrix.m_matrix)){}
    //destructor
    ~ Matrix() = default;
    // instantiate an object
    static Matrix Input(int row, int col){
        Matrix m(row, col);
        std::cout << "enter the matrix: " << std::endl;
        for(int i = 0; i < row; ++i){
            for(int j = 0; j < col; ++j){
                std::cin >> m.m_matrix[i][j];
            }
        }
        return m;
    }
    static Matrix Identity(int row){
        Matrix m(row, row);
        for(int i = 0; i < row; ++i){
            m.m_matrix[i][i] = 1;
        }
        return m;
    }

    // get information
    void print() const{
        std::cout << "[";
        for(int i = 0; i < this->row; ++i){
            std::cout << "[";
            for(int j = 0; j < this->col; ++j){
                std::cout << this->m_matrix[i][j];
                if(j != this->col-1){
                    std::cout << " ";
                }else{
                    std::cout << "]";
                }
            }

            if(i != this->row-1){
                std::cout << std::endl;
            }
        }
        std::cout << "]" <<std::endl;
    }

    // operator override
    const std::vector<float>& operator[](const int row) const{
        return this->m_matrix[row];
    }
    std::vector<float>& operator[](const int row){
        return this->m_matrix[row];
    }

    Matrix& operator=(const Matrix& other){
        if(&other == this){
            return *this;
        }
        this->row = other.row;
        this->col = other.col;
        this->m_matrix = other.m_matrix;
        return *this;
    }
    Matrix& operator=(Matrix&& other) noexcept{
        if(&other == this){
            return *this;
        }
        this->row = other.row;
        this->col = other.col;
        this->m_matrix = std::move(other.m_matrix);
        return *this;
    }
    Matrix operator+(const Matrix& other) const{
        if(this->row != other.row || this->col != other.col){
            throw std::invalid_argument("matrix size unmatched.");
        }
        Matrix m(this->row, this->col);
        for(int i = 0; i < this->row; ++i){
            for(int j = 0; j < this->col; ++j){
                m.m_matrix[i][j] = this->m_matrix[i][j] + other.m_matrix[i][j];
            }
        }
        return m;
    }
    Matrix operator-(const Matrix& other) const{
        if(this->row != other.row || this->col != other.col){
            throw std::invalid_argument("matrix size unmatched.");
        }
        Matrix m(this->row, this->col);
        for(int i = 0; i < this->row; ++i){
            for(int j = 0; j < this->col; ++j){
                m.m_matrix[i][j] = this->m_matrix[i][j] - other.m_matrix[i][j];
            }
        }
        return m;
    }
    Matrix operator*(const Matrix& other) const{
        if(this->col != other.row){
            throw std::invalid_argument("uncomputable matrices.");
        }
        Matrix m(this->row, other.col);
        for(int i = 0; i < this->row; ++i){
            for(int k = 0; k < this->col; ++k){
                for(int j = 0; j < other.col; ++j){
                    m.m_matrix[i][j] += this->m_matrix[i][k]*other.m_matrix[k][j];
                }
            }
        }
        return m;
    }
};

int main(){
    Matrix m1 = Matrix::Input(3, 3);
    Matrix m2 = Matrix::Identity(3);
    m1.print();
    Matrix m3 = m1 + m2;
    m1 = m1*m3;
    m1.print();

    return 0;
}