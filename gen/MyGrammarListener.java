// Generated from /Users/arne/Documents/repos/school/Compiler/src/antlr_files/project_1/MyGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MyGrammarParser}.
 */
public interface MyGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MyGrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MyGrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(MyGrammarParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(MyGrammarParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#logicalExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalExpression(MyGrammarParser.LogicalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#logicalExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalExpression(MyGrammarParser.LogicalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#comparisonExpression}.
	 * @param ctx the parse tree
	 */
	void enterComparisonExpression(MyGrammarParser.ComparisonExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#comparisonExpression}.
	 * @param ctx the parse tree
	 */
	void exitComparisonExpression(MyGrammarParser.ComparisonExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(MyGrammarParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(MyGrammarParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(MyGrammarParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(MyGrammarParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#bitwiseExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseExpression(MyGrammarParser.BitwiseExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#bitwiseExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseExpression(MyGrammarParser.BitwiseExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void enterShiftExpression(MyGrammarParser.ShiftExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void exitShiftExpression(MyGrammarParser.ShiftExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpression(MyGrammarParser.UnaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpression(MyGrammarParser.UnaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyGrammarParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(MyGrammarParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyGrammarParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(MyGrammarParser.PrimaryContext ctx);
}