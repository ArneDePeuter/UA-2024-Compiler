// Generated from /Users/arne/Documents/repos/school/Compiler/src/antlr_files/project_1/MyGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MyGrammarParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MyGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MyGrammarParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(MyGrammarParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#logicalExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalExpression(MyGrammarParser.LogicalExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#comparisonExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparisonExpression(MyGrammarParser.ComparisonExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#additiveExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditiveExpression(MyGrammarParser.AdditiveExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicativeExpression(MyGrammarParser.MultiplicativeExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#bitwiseExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitwiseExpression(MyGrammarParser.BitwiseExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#shiftExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShiftExpression(MyGrammarParser.ShiftExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#unaryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryExpression(MyGrammarParser.UnaryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyGrammarParser#primary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimary(MyGrammarParser.PrimaryContext ctx);
}