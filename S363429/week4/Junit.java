import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;

public class CalculatorTest {
    
    private Calculator calculator;

    // 在每个测试方法之前运行
    @Before
    public void setUp() {
        calculator = new Calculator();
    }

    // 测试加法方法
    @Test
    public void testAddition() {
        assertEquals(5, calculator.add(2, 3));
    }

    // 测试减法方法
    @Test
    public void testSubtraction() {
        assertEquals(1, calculator.subtract(3, 2));
    }
}
